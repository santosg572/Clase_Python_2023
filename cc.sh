#!/bin/bash

python crea_examen.py ${1}
pdflatex ${1}.tex


