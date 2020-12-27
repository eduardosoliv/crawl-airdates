# Crawl Airdates.tv Export Series

Crawls [Airdates.tv](https://www.airdates.tv/) and uses [OMDb API](http://www.omdbapi.com/) to fetch information such as IMDB rating. Requires API access to OMDb API ([free 1000 daily limit](http://www.omdbapi.com/apikey.aspx)).

## Install

To install dependencies use [poetry](https://python-poetry.org/docs/):
```
poetry install
```

## Usage

To use:
```
$ python exportseries/main.py --help
Usage: main.py [OPTIONS]

Options:
  --apikey TEXT          OMDb API Key  [required]
  --outputfilename TEXT  Name of file to output CSV, default dump.csv
  --help                 Show this message and exit.
```

Example:
```
$ python exportseries/main.py --apikey yourkey
$ wc -l dump.csv 
288 dump.csv
$ head -5 dump.csv 
Search Name,Title,IMDB Rating,IMDB Votes,IMDB ID,IMDB URL,Year,Language,Country,Genre
The Flight Attendant ,The Flight Attendant,7.3,605,tt7569576,https://www.imdb.com/title/tt7569576,2020–,English,USA,"Comedy, Drama, Mystery, Thriller"
Real Housewives of Cheshire,The Real Housewives of Cheshire,4.3,231,tt4455862,https://www.imdb.com/title/tt4455862,2015–,English,UK,Reality-TV
Don't Be Tardy,Don't Be Tardy...,4.5,264,tt2176353,https://www.imdb.com/title/tt2176353,2012–,English,USA,Reality-TV
RuPaul's Drag Race UK,RuPaul's Drag Race UK,8.3,"1,788",tt9780442,https://www.imdb.com/title/tt9780442,2019–,N/A,UK,"Game-Show, Reality-TV"
```

## Run tests

To run tests:
```
pytest
```

To check coverage
```
coverage run -m --source=. pytest
coverage report -m
```
