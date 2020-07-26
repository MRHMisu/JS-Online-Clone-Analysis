const espree = require("espree");

const fs = require('fs');
const csv = require('csv-parser');
const acceptedCodeSnippet = "/home/mrhmisu/Downloads/js_accepted_code_snippet_min10Lines.csv";
//const acceptedCodeSnippet = "/home/mrhmisu/Downloads/demo.csv";
const outputDirectory = "/home/mrhmisu/Downloads/Data";


function readCodeSnippets(path, outputDir) {
    var validCodeCounter = 0;
    var totalCodeCounter = 0;

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
    // Set to 3, 5 (default), 6, 7, 8, 9, or 10 to specify the version of ECMAScript syntax you want to use.
    // You can also set to 2015 (same as 6), 2016 (same as 7), 2017 (same as 8), 2018 (same as 9),
    // 2019 (same as 10), or 2020 (same as 11) to use the year-based naming.
    const features = {
        // enable JSX parsing
        jsx: false,
        // enable return in global scope
        globalReturn: false,
        // enable implied strict mode (if ecmaVersion >= 5)
        impliedStrict: false
    }
    const version = 2020;

    try {
        const astScript = espree.parse(sourceCode, {
            range: true,
            ecmaVersion: version,
            sourceType: "script",
            ecmaFeatures: features
        });
        if (astScript != null) return true;
    } catch (expScript) {
        try {
            const astModule = espree.parse(sourceCode, {
                range: true,
                ecmaVersion: version,
                sourceType: "module",
                ecmaFeatures: features
            });
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

readCodeSnippets(acceptedCodeSnippet, outputDirectory);