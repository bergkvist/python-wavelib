#! /usr/bin/env nix-shell
#! nix-shell ../shell.nix -i bash

VERSION="$(python setup.py --version)"

python setup.py sdist

twine upload \"dist/wavelib-$VERSION.tar.gz\"
