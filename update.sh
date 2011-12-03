#!/bin/sh
ROOT="sources"
zim --export --output=./ --format=html --template=./template.html "$ROOT"
cp Stanford.html index.html
git add sources Stanford Stanford.html index.html
git commit -am "actualizacón automatica"
git push
