#!/bin/sh

set -e

echo y | sudo pip uninstall londinium
sudo python3 setup.py install
sudo rm -rf docs/source/londinium.*.rst
sudo rm -rf docs/source/modules.rst
sphinx-apidoc -feM -d 1 -o docs/source .
#sed -i "s/.. toctree::/.. toctree::\n   :maxdepth: 1/g" doc/source/londinium.*
sed -i "s/    /   /g" docs/source/londinium.*
sphinx-build -b html docs/source/ ../../../../Websites/docpages/beautfl/londinium
