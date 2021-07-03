#! /usr/bin/env nix-shell
#! nix-shell ../shell.nix -i bash

python setup.py build_ext --build-lib=.
pytest test.py || true
rm -rf build __pycache__ .pytest_cache *.so