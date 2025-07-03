#!/bin/bash
# sh build.sh <dirname> <--release or empty>

NAME="$1"
cd "$NAME"

OPTION="$2"
if [ -z "$OPTION" ]; then
    maturin build
else
    maturin build "$OPTION"
fi

pip install target/wheels/"$NAME"-*.whl