/**
 * This script takes a  locally stored JavaScript repository path  and validate each '.js' file with
 * the ESLint parser ESPree.
 *
 * How to run the script
 * ~:node Git-JS-Repository-Validator.js repositoryPath
 */

'use strict'

const path = require("path");
const fs = require("fs");
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

function validateEachRepository(baseDirPath, projectName) {
    const repositoryPath = baseDirPath + "/" + projectName
    const jsFilter = "js";
    const jsxFilter = "jsx"
    let jsFiles = filterSourceFiles(repositoryPath, jsFilter);
    let jsxFiles = filterSourceFiles(repositoryPath, jsxFilter);
    let allFiles = [...jsFiles, ...jsxFiles];

    const totalFiles = allFiles.length;
    let nonParsedFiles = 0;
    let parsedFiles = 0;
    allFiles.forEach(function (filepath) {
        let content = fs.readFileSync(filepath).toString();
        if (isValidCodeSnippet(content, filepath))
            parsedFiles++;
        else
            nonParsedFiles++;
    });
    return repositoryPath + "," + projectName + "," + totalFiles + "," + parsedFiles + "," + nonParsedFiles + "\n";

}

function isValidCodeSnippet(sourceCode, filePath) {

    const scriptMood = "script";
    const moduleMood = "module";

    if (!isValidated(sourceCode, scriptMood)) {
        if (!isValidated(sourceCode, moduleMood)) {
            console.log(filePath);
            return false;
        }
        return true;
    }
    return true;
}

function isValidated(sourceCode, sourceType) {
    try {
        const astScript = espree.parse(sourceCode, {
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

function filterSourceFiles(startPath, filter) {
    let fileList = [];
    traverseDirectory(startPath, filter, fileList);
    return fileList;

}

function traverseDirectory(baseDirPath, filter, fileList) {
    let files = fs.readdirSync(baseDirPath);
    for (let i = 0; i < files.length; i++) {
        let filename = path.join(baseDirPath, files[i]);
        let stat = fs.lstatSync(filename);
        let extension = filename.split(".").pop().trim();
        if (stat.isDirectory()) {
            traverseDirectory(filename, filter, fileList);
        } else if (extension === filter) {
            fileList.push(filename);
        }
    }
}

function isValidFileAndDirectory(baseDirPath, projectList) {
    if (fs.existsSync(projectList) && fs.existsSync(baseDirPath)) return true;
    return false;
}


function validateRepositories(baseDirPath, projectListFile) {
    let results = [];
    let header = "repositoryPath, project_name, total_files, parsed_files, non_parsed_files\n";
    results.push(header);
    let outputPath = baseDirPath + "/" + "parsedResult.csv"
    const data = fs.readFileSync(projectListFile, 'UTF-8');
    let lines = data.split(/\r?\n/);
    const projects = lines.filter(e => e);
    projects.forEach((p) => {
        let projectResult = validateEachRepository(baseDirPath, p);
        results.push(projectResult);
    });

    let processedResult = results.join("")
    fs.writeFile(outputPath, processedResult, function (err) {
        if (err) return console.log(err);
        console.log("Result Saved to " + outputPath);
    });
}


function executeScript() {
    let cmdArguments = process.argv.slice(2);
    let projectListFile = cmdArguments[0];
    let baseDirPath = cmdArguments[0];
    if (isValidFileAndDirectory(baseDirPath, projectListFile)) {
        validateRepositories(baseDirPath, projectListFile)
    }
}

executeScript();

