#!/bin/bash

base_path=/home/ubuntu/

while IFS='' read -r line || [[ -n "$line" ]]; do

  # remove all duplicate files
  rdfind -deleteduplicates true $base_path/$line

  # remove all node_modules directory
  #find . -name "node_modules"
  # find . -type d -name 'node_modules' -exec rm -r {} +


done \
  <"$1"
