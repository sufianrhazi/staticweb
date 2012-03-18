#!/bin/bash

for template in www/*.tml; do
    PYTHONPATH=./lib/python ./scripts/compile_jinja.py variables.json $template
done

for template in www/css/*.scss; do
    ./scripts/compile_scss.sh $template
done
