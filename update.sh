#!/bin/sh
ROOT="sources"
zim --export --output=./ --format=html --template=./template.html "$ROOT"
git add sources Stanford Stanford.html
git commit -am "actualizacón automatica"
git push
