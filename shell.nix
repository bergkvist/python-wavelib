let
    pkgs = import <nixpkgs> {};
in pkgs.mkShell {
    LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [ pkgs.stdenv.cc.cc.lib ];
    buildInputs = [
        pkgs.stdenv.cc.cc.lib
        pkgs.entr
        pkgs.python39
        pkgs.python39.pkgs.pybind11
        pkgs.python39.pkgs.numpy
        pkgs.python39.pkgs.setuptools
        pkgs.python39.pkgs.pytest
        pkgs.python39.pkgs.twine
    ];
}