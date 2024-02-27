#!/bin/bash

# Download natural language data
mkdir natural
(
    cd natural || exit
    wget https://www.corpusdata.org/coca/samples/coca-samples-text.zip
    unzip coca-samples-text.zip
)

# Download code data
mkdir code
(
    cd code || exit
    git clone https://github.com/zulip/zulip.git
    git clone https://github.com/qt-creator/qt-creator.git
    git clone https://github.com/servo/servo.git
)
