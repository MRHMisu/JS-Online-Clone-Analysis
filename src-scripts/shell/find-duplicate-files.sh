#!/bin/bash

result[0]="repo_name, duplicate_files"$'\n'
counter=0

while IFS='' read -r line || [[ -n "$line" ]]; do
  echo $line
  echo "Finding duplicate in the directory $line"
  rdfind ./"$line"
  echo "Renaming the results.txt file to $line-duplicate-files.txt"
  mv results.txt "$line-duplicate-files.txt"
  echo "Moving $line-duplicate-files.txt to the directory->./$line"
  mv "$line-duplicate-files.txt" ./$line
  duplicateFiles=$(wc -l ./$line/"$line-duplicate-files.txt")
  echo $duplicateFiles

  counter="$(($counter + 1))"
  for word in $duplicateFiles; do
    value="$(($word - 3))"
    result[$counter]=$(printf "$line,$value\r\n")
    echo "${result[$counter]}"
    break
  done
done <"$1"

echo "${result[*]}" >duplicate-file-statistics.csv
