#! /usr/bin/env nix-shell
#! nix-shell ../shell.nix -i bash

ls | entr -cs "bash scripts/test.sh"