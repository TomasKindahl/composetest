#!/bin/bash
echo "# composetest" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/TomasKindahl/composetest.git
git config credential.helper store
git push -u origin main

