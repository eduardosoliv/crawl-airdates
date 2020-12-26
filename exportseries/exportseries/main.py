import requests
from bs4 import BeautifulSoup
import click
import urllib
import csv

airdates_baseurl = 'https://www.airdates.tv/'
omdbapi_baseurl = 'http://www.omdbapi.com/'

def get_page(url):
    page = requests.get(url)
    if not page.ok:
      raise Exception("Error, unable to fetch " + url + " status code " + str(page.status_code))
    return page

def extract_serie_name(serie_name):
  return serie_name.rsplit(' ', 1)[0]

def get_series(content):
    soup = BeautifulSoup(content, 'html.parser')
    series = set()
    for elem in soup.findAll("div", {"class": "title"}):
        series.add(extract_serie_name(elem.text))
    if series == set():
        raise Exception("Error, unable to find series on page content")
    return series

def get_serie_data(series_name, apikey):
  omdbapi_args = urllib.parse.urlencode({ 't' : series_name, 'apikey' : apikey})
  return get_page(omdbapi_baseurl + '?' + omdbapi_args).json()

def write_csv(series, outputfilename, apikey):
  with open(outputfilename, 'w', newline='') as outputfile:
    writer = csv.writer(outputfile)
    writer.writerow([
      'Search Name',
      'Title',
      'IMDB Rating',
      'IMDB Votes',
      'IMDB ID',
      'IMDB URL',
      'Year',
      'Language',
      'Country',
      'Genre'
    ])
    for serie_name in series:
      serie_data = get_serie_data(serie_name, apikey)
      imdbid = serie_data.get('imdbID','')
      imdburl = ''
      if imdbid:
        imdburl = 'https://www.imdb.com/title/' + imdbid
      writer.writerow([
        serie_name,
        serie_data.get('Title',''),
        serie_data.get('imdbRating',''),
        serie_data.get('imdbVotes',''),
        imdbid,
        imdburl,
        serie_data.get('Year',''),
        serie_data.get('Language',''),
        serie_data.get('Country',''),
        serie_data.get('Genre',''),
      ])

@click.command()
@click.option('--apikey', required=True, help='OMDb API Key')
@click.option('--outputfilename', default='dump.csv', help='Name of file to output CSV, default dump.csv')
def get_ratings(apikey, outputfilename):
  airdates = get_page(airdates_baseurl)
  series = get_series(airdates.content)
  write_csv(series, outputfilename, apikey)

if __name__ == "__main__":
  get_ratings()