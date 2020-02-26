#!/bin/sh

set -e

sphinx-build -E -a -b html home .
cp -r home/_static/* _static
