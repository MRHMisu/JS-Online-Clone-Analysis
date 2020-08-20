const fs = require('fs');
const csv = require('csv-parser');
const eslint = require('eslint')
const Linter = require("eslint").Linter;
const linter = new Linter();

//const acceptedCodeSnippet = "/home/mrhmisu/Downloads/js_accepted_code_snippet_min10Lines.csv";
const acceptedCodeSnippet = "/home/mrhmisu/Downloads/demo.csv";
const outputDirectory = "/home/mrhmisu/Downloads/Data";


function readCodeSnippets(path, outputDir) {
    const cli = getESLintCLIEngine();
    var counter = 0;
    var i = 0;
    fs.createReadStream(path)
        .pipe(csv())
        .on('data', function (row) {
            let codeSnippet = covertHexStringToAscii(row['code_snippet']);
            if (isValidCodeSnippet(cli, codeSnippet)) {
                let questionId = row['question_id'];
                let answerId = row['answer_id'];
                let fileName = counter + "_" + questionId + "_" + answerId + ".js";
                let filePath = outputDir + "/" + fileName;
                //writeValidatedCodeSnippet(codeSnippet, filePath);
                console.log("Counter=>" + counter + '\n');
                counter++;
            }

        })
        .on('end', function () {
            console.log(counter);
            console.log("Code Snippet Filtering Done.");

        })

}

function covertHexStringToAscii(hexString) {
    let hex = hexString.toString();//force conversion
    let str = '';
    for (let i = 0; (i < hex.length && hex.substr(i, 2) !== '00'); i += 2)
        str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    return str;
}

function isValidCodeSnippet(cli, sourceCode) {
    var fixableErrorCount = cli.executeOnText(sourceCode).fixableErrorCount;
    var errorCount = cli.executeOnText(sourceCode).errorCount;
    var result = cli.executeOnText(sourceCode).results;
    //console.log(sourceCode);
    if ((errorCount == 0)) {
        return true;
    }
    return false;
}

function getESLintCLIEngine() {
    var CLIEngine = eslint.CLIEngine
    var cli = new CLIEngine({
        useEslintrc: false,
        configFile: 'eslintrc.json'
    });
    return cli;
}

function writeValidatedCodeSnippet(content, fileName) {
    fs.writeFile(fileName, content, function (err) {
        if (err) throw err;
        console.log('Saved!');
    });
}

function validateScript(sourceCode, config) {
    const messages = linter.verify(sourceCode, config, {filename: "foo.js"});
    if (messages.length != 0) return true;
    return false;
}

function getConfigRules() {
    let lintConfig = fs.readFileSync('eslintrc.json');
    let config = JSON.parse(lintConfig);
    return config['rules'];
}

readCodeSnippets(acceptedCodeSnippet, outputDirectory);
