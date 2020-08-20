#!/bin/bash

find . -name "node_modules" > all_node_modules_directory.txt
while IFS='' read -r line || [[ -n "$line" ]]; do
  echo "Removing node_modules from the repository $line"
  find ./"$line" -name "node_modules"
  find ./"$line" -type d -name 'node_modules' -exec rm -r {} +
  echo "Successfully done"
done <"$1"
