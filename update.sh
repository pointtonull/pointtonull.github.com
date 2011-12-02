#!/bin/sh
ROOT="sources"
zim --export --output=./ --format=html --template=./template.html "$ROOT"
