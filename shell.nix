{ pkgs ? import <nixpkgs> {} }:

let
  python-version = pkgs.python312;

  
  python-env = python-version.withPackages (ps: with ps; [
    # requests
    # numpy
    # pandas
    pytest
  ]);

in

pkgs.mkShell {
  buildInputs = [
    python-env
  ];

  # Environment variables
  # shellHook = ''
  #   export PYTHONPATH="$PWD"
  # '';
}