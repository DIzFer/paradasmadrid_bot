with import <nixpkgs> {};
stdenv.mkDerivation rec {
  name = "paradasmadrid_bot";
  env = buildEnv { name = name; paths = buildInputs; };
  buildInputs = with python3Packages; [
    # Lo obvio
    python3
    python-telegram-bot
    # Queremos código bonito y consistente
    pylint
    autopep8
    # Dependencias
    requests
  ];
}
