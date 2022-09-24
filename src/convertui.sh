#!/bin/bash

# Developed by Romerito Morais using QtDesigner + Python3.10
# To work it is necessary to have installed the following libs:

# define path do projeto
path=$(pwd)

# convert o novo .ui para um novo form na raiz do projeto
pyuic5 $path/qtdesigner/principal.ui -o $path/main.py