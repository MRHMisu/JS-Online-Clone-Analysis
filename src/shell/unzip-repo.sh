#!/bin/bash

while IFS='' read -r line || [[ -n "$line" ]]; do
  echo $line
  echo "unziping $line"
  mkdir $line
  python unzip.py "$line.zip" ./"$line"
  echo "Successfully Done"
done <"$1"