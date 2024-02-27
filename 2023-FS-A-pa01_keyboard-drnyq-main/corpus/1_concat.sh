#!/bin/bash

echo "A big corpus of text and code" >big_corpus.txt

find . -type f | while read -r fname; do
    if file "$fname" | grep "text" &>/dev/null; then
        cat "$fname" >>big_corpus.txt
    # else
    #     file "$fname"
    fi
done
