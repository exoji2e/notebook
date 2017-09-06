#!/bin/bash
pdflatex -shell-escape notebook
pdflatex -shell-escape notebook
rm *.aux
rm *.toc
rm -r _minted-notebook
rm *.log
