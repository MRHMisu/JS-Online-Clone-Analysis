# JS-Online-Clone-Analysis
It is a utility repository for the JS-Online-Clone-Analysis between Stack Overflow and GitHub Repositories. It contains all the source code and scripts that was created and utilised in the Replication Study. It contains three packages python, javaScript and shell. 

* python package contains the scripts for downloading, extracting and analysing the Stack Overflow data dump. 
* javaScript package contains the script for validating Stack Overflow and GitHub snippets with ESLint, Espree and JSHint. 
* Furthermore, the shell package contains Unix scripts that help to remove duplicate files, remove unnecessary directories. Additionally, this repository contains the script for producing the raw results

* The manually validated clone pairs can be found into this web application [JS-Online-Clone-Classifier](https://js-online-clone.web.app/)
* Complete dataset is published here [JS-Online-Clone-Analysis-Dataset](https://drive.google.com/drive/folders/1ej0zavvPoaeJjfHu_nLD4pxH2eZVb57T).
  This dataset contains the following  directories and files.
 
```
.
└── JS-Online-Clone-Analysis-Data
    ├── clone_pair
    │   ├── 14343_pair_statistic.txt
    │   ├── 1466_filtered_clone_pairs_statistics.txt
    │   ├── 6444_filtered_pairs_len_ratio.csv
    │   ├── 6444_filtered_pairs_statistics.txt
    │   └── js-online-clone-pairs-1466.json
    ├── developed-js-corpus
    │   ├── 1466-Manually-Validated-Clone-Pairs.xlsx
    │   ├── cloc-output-after-filtering.txt
    │   ├── cloc-output-before-filtering.txt
    │   ├── complete-js-online-clone-analysis-dataset.xlsx
    │   ├── downloaded_repositories.txt
    │   ├── duplicate-file-statistics-after-filtering.xlsx
    │   ├── duplicate-file-statistics-before-filtering.xlsx
    │   ├── javascript-github-projects-statistics.xlsx
    │   ├── syntax-validation-after-duplicate-node-modules-removing.xlsx
    │   └── syntax-validation-before-duplicate-node-modules-removing.xlsx
    ├── frequency
    │   ├── java-snippet-frequency.xlsx
    │   ├── js-snippet-frequency.xlsx
    │   └── python-snippet-frequency.xlsx
    └── so-snippets
        ├── js-so-accepted-code-snippet.csv
        ├── python-so-accepted-code-snippet.csv
        └── so-syntactically-validated-js-snippets.tar.gz
        
```