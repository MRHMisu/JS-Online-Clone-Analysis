/**
 *
 * The provided 'soFilteredCodeSnippetPath' csv file should contains the following 5 columns
 * CSV Header => [question_id, answer_id, block_position, loc, code_snippet]
 *
 *
 */

const fs = require('fs');
const csv = require('csv-parser');
const espree = require("espree");

const features = {
    // enable JSX parsing
    jsx: true,
    // enable return in global scope
    globalReturn: true,
    // enable implied strict mode (if ecmaVersion >= 5)
    impliedStrict: true
}

/**
 *Set a version typically the released year
 * 2015->ES6, 2016->ES7, 2017->ES8,
 * 2018->ES9, 2019->ES10, 2020->ES11
 */
const ecmaVersion = 2017;

/**
 *
 * @param soFilteredCodeSnippetPath
 * @param outputDirectoryPath
 */
function validateSOJSCodeSnippets(soFilteredCodeSnippetPath, outputDirectoryPath, loc) {
    let totalCodeSnippets = 0;
    let validCodeSnippets = 0;
    let inValidCodeSnippets = 0;

    fs.createReadStream(soFilteredCodeSnippetPath)
        .pipe(csv())
        .on('data', function (row) {
            totalCodeSnippets++;
            let codeSnippet = covertHexStringToAscii(row['code_snippet']);
            let snippetLength = row['loc'];
            if (snippetLength >= loc) {
                if (isValidatedCodeSnippet(codeSnippet)) {
                    let fileName = row['question_id'] + "_" + row['block_position'] + ".js";
                    let filePath = outputDirectoryPath + "/" + fileName;
                    writeValidatedCodeSnippet(codeSnippet, filePath);
                    validCodeSnippets++;
                } else
                    inValidCodeSnippets++;

            }
        })
        .on('end', function () {
            printStatistic(totalCodeSnippets, validCodeSnippets, inValidCodeSnippets);
        });

}


function isValidatedCodeSnippet(sourceSnippet) {
    const scriptMood = "script";
    const moduleMood = "module";

    if (!isValidated(sourceSnippet, scriptMood)) {
        if (!isValidated(sourceSnippet, moduleMood)) {
            return false;
        }
        return true;
    }
    return true;
}

function covertHexStringToAscii(hexString) {
    let hex = hexString.toString();//force conversion
    let str = '';
    for (let i = 0; (i < hex.length && hex.substr(i, 2) !== '00'); i += 2)
        str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    return str;
}

function isValidated(sourceSnippet, sourceType) {
    try {
        const astScript = espree.parse(sourceSnippet, {
            range: true,
            ecmaVersion: ecmaVersion,
            sourceType: sourceType,
            ecmaFeatures: features
        });
        if (astScript != null) return true;
        else return false;
    } catch (exp) {
        return false;
    }
}


function isValidFileAndDirectoryAndLOC(soFilteredCodeSnippetPath, outputDirectoryPath, loc) {
    if (fs.existsSync(outputDirectoryPath) && fs.existsSync(soFilteredCodeSnippetPath) && loc > 0) return true;
    return false;
}

function printStatistic(totalCodeSnippets, validCodeSnippets, inValidCodeSnippets) {
    console.log("#########################################################")
    console.log("Total Code-Snippets:=" + totalCodeSnippets);
    console.log("Valid Code-Snippets:=" + validCodeSnippets);
    console.log("Invalid Code-Snippets:=" + inValidCodeSnippets);
    console.log("#########################################################")
}

function writeValidatedCodeSnippet(content, fileName) {
    fs.writeFile(fileName, content, function (err) {
        if (err) throw err;
        console.log(fileName + ' is saved');
    });
}

function executeScript() {
    let cmdArguments = process.argv.slice(2);
    let soFilteredCodeSnippetPath = cmdArguments[0];
    let outputDirectoryPath = cmdArguments[1];
    let loc = cmdArguments[2];
    if (isValidFileAndDirectoryAndLOC(soFilteredCodeSnippetPath, outputDirectoryPath, loc)) {
        validateSOJSCodeSnippets(soFilteredCodeSnippetPath, outputDirectoryPath, loc);
    } else {
        console.log("Invalid Arguments");
    }
}

executeScript();