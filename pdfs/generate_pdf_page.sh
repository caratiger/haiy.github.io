#!/bin/bash
file_list=$(ls)
for f in $file_list;
do
    echo "<a target='_blank' href=pdfs/$f>${f%.pdf}</a>" >> pdfs.html
done
