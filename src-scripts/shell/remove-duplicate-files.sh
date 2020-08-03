#!/bin/bash

while IFS='' read -r line || [[ -n "$line" ]]; do
  echo "Removing Duplicate files from directory $line"
  # remove all duplicate files
  rdfind -deleteduplicates true ./"$line"
  echo "Successfully done"
done <"$1"