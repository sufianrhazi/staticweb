#!/bin/bash

if [ "$1" == "" -o "${1: -5}" != ".scss" ]; then
    echo "Usage $0 <input.scss>"
    echo "Writes to <input.css>"
    exit 1
fi

target=${1/.scss/.css}
echo "Building ${target}..."
sass=lib/ruby/gems/sass-*/bin/sass
${sass} --trace $1 ${target}
