#!/bin/sh
ROOT="sources"
zim --export --output=./ --format=html --template=./template.html "$ROOT"
cp home.html index.html
git add sources index home.html index.html
git commit -am "actualizacón automatica"
git push
