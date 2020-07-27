var jshint = require("jshint");

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

    //https://jshint.com/docs/options/
    const options = {
        undef: true,
        esversion: 11
    };
    const predef = {};
    try {
        jshint.JSHINT(sourceCode, options, predef);
        const errors = jshint.JSHINT.errors;
        if (errors.length == 0) return true;
    } catch (exp) {
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