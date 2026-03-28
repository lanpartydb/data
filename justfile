_default:
    @just --list

fetch-contributors:
    @python3 tools/fetch_contributors.py > data/contributors.json

validate: && validate-series validate-parties validate-party-dates

validate-series:
    @echo "\nValidating series ..."
    @taplo lint --schema "file://"$PWD"/schemas/series.json" data/series/*.toml && taplo format --check data/series/*.toml

validate-parties:
    @echo "\nValidating parties ..."
    @taplo lint --schema "file://"$PWD"/schemas/party.json" data/parties/**/*.toml && taplo format --check data/parties/**/*.toml

validate-party-dates:
    @echo "\nValidating party dates ..."
    @python3 tools/check_party_date.py data/parties/**/*.toml
