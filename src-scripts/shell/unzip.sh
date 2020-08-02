#!/bin/bash

while IFS='' read -r line || [[ -n "$line" ]]; do
  echo $line
  echo "unziping $line"
  mkdir $line
  unzip "$line.zip" -d ./"$line"
  echo "Successfully Done"
done <"$1"
