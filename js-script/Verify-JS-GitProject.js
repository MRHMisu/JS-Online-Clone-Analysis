const path = require("path");
const fs = require("fs");
const espree = require("espree");

const baseDir = "/home/mrhmisu/UCL-MS/Test-Data/Download-JS-Reop/freeCodeCamp-master";


validateProject(baseDir);


function validateProject(baseDir) {
    let nonParsedFile = 0;
    const filter = "js";
    var files = getJSFiles(baseDir, filter);
    files.forEach(function (filepath) {
        var content = fs.readFileSync(filepath).toString();
        if (!isValidCodeSnippet(content, filepath)) {
            nonParsedFile++;
        }
    });
    console.log(files.length + " Source Files Found")
    console.log(nonParsedFile + " files can not be parsed");
}


function isValidCodeSnippet(sourceCode, filePath) {
    // Set to 3, 5 (default), 6, 7, 8, 9, or 10 to specify the version of ECMAScript syntax you want to use.
    // You can also set to 2015 (same as 6), 2016 (same as 7), 2017 (same as 8), 2018 (same as 9),
    // 2019 (same as 10), or 2020 (same as 11) to use the year-based naming.
    const features = {
        // enable JSX parsing
        jsx: true,
        // enable return in global scope
        globalReturn: false,
        // enable implied strict mode (if ecmaVersion >= 5)
        impliedStrict: true
    }
    const version = 2017;

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
            if (astModule != null) {
                //console.log("return true by treated as Module");
                return true;

            }
        } catch (expModule) {
            console.log(filePath);
            return false;
        }
        return false;
    }
    return false;
}


function getJSFiles(startPath, filter) {
    var fileList = [];
    fromDir(startPath, filter, fileList);
    return fileList;

}

function fromDir(startPath, filter, fileList) {
    //console.log('Starting from dir '+startPath+'/');
    if (!fs.existsSync(startPath)) {
        console.log("no dir ", startPath);
        return;
    }
    var files = fs.readdirSync(startPath);
    for (var i = 0; i < files.length; i++) {
        var filename = path.join(startPath, files[i]);
        var stat = fs.lstatSync(filename);
        var extention = filename.split(".").pop().trim();
        if (stat.isDirectory()) {
            fromDir(filename, filter, fileList); //recurse
        } else if (extention === filter) {
            fileList.push(filename);
        }
    }
}
