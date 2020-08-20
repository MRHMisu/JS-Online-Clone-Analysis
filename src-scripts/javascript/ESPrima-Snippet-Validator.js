const esprima = require('esprima');
const fs = require('fs');
const csv = require('csv-parser');

const acceptedCodeSnippet = "/home/mrhmisu/Downloads/js_accepted_code_snippet_min10Lines.csv";
//const acceptedCodeSnippet = "/home/mrhmisu/Downloads/demo.csv";
const outputDirectory = "/home/mrhmisu/Downloads/Data";

// run the script
readCodeSnippets(acceptedCodeSnippet, outputDirectory);


function readCodeSnippets(path, outputDir) {
    let validCodeCounter = 0;
    let totalCodeCounter = 0;

    fs.createReadStream(path)
        .pipe(csv())
        .on('data', function (row) {
            totalCodeCounter++;
            let codeSnippet = covertHexStringToAscii(row['code_snippet']);
            if (isValidCodeSnippet(codeSnippet)) {
                let questionId = row['question_id'];
                let answerId = row['answer_id'];
                let fileName = validCodeCounter + "_" + questionId + "_" + answerId + ".js";
                let filePath = outputDir + "/" + fileName;
                //writeValidatedCodeSnippet(codeSnippet, filePath);
                console.log("Counter=>" + validCodeCounter);
                validCodeCounter++;
            }
            //console.log(i + '\n');
            //i++;

        })
        .on('end', function () {
            console.log("Total Code Snippet:=" + totalCodeCounter + '\n');
            console.log("Valid Code Snippet:=" + validCodeCounter + '\n');
            console.log("Invalid Code Snippet:=" + (totalCodeCounter - validCodeCounter + '\n'));

        })

}

function covertHexStringToAscii(hexString) {
    let hex = hexString.toString();//force conversion
    let str = '';
    for (let i = 0; (i < hex.length && hex.substr(i, 2) !== '00'); i += 2)
        str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    return str;
}

function isValidCodeSnippet(sourceCode) {
    //https://esprima.readthedocs.io/en/latest/syntactic-analysis.html
    // supported version upto ECMAScript-2017 (ECMAScript-8)
    const options = {
        //Support JSX syntax
        jsx: true,
        //Annotate each node with its index-based location
        range: true,
        // Annotate each node with its column and row-based location
        loc: false,
        // Tolerate a few cases of syntax errors
        tolerant: true,
        // Collect every token
        tokens: false,
        // Collect every line and block comment
        comment: false

    };
    try {
        const astScript = esprima.parseScript(sourceCode, options);
        if (astScript != null) return true;
    } catch (expScript) {
        try {
            const astModule = esprima.parseModule(sourceCode, options);
            if (astModule != null) return true;
        } catch (expModule) {
            return false;
        }
        return false;
    }
    return false;
}


function writeValidatedCodeSnippet(content, fileName) {
    fs.writeFile(fileName, content, function (err) {
        if (err) throw err;
        console.log('Saved!');
    });
}


