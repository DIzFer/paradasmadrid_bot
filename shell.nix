with import <nixpkgs> {};
stdenv.mkDerivation rec {
  name = "paradasmadrid_bot";
  env = buildEnv { name = name; paths = buildInputs; };
  buildInputs = [
    python3
    python3Packages.python-telegram-bot
    python3Packages.pylint
    python3Packages.autopep8
  ];
}
