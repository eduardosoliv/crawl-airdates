# Crawl Airdates.tv Fetch Premieres

Crawls [Airdates.tv](https://www.airdates.tv/) and prints series/season premieres.

## Install

To install dependencies use [poetry](https://python-poetry.org/docs/):
```
poetry install
```

## Usage

To use:
```
$ python premieres/main.py --help
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.

  --help                Show this message and exit.

Commands:
  season
  series
```

Example:
```
$ python premieres/main.py series
The Challenge
The Mess You Leave Behind
The Wilds
Tiny Pretty Things
The Ripper
The Stand
Bridgerton
Call Me Kat
The Great North
The Watch
History of Swear Words
Coyote
Mr. Mayor
Lupin
Call Your Mother
WandaVision
Walker
Fate: The Winx Saga
Resident Alien
Firefly Lane
The Equalizer (2021)
Clarice
Superman & Lois
```

## Run tests

To run tests:
```
pytest
```

To check coverage:
```
coverage run -m --source=. pytest
coverage report -m
```
