import typer
import requests
from bs4 import BeautifulSoup

airdates_baseurl = 'https://www.airdates.tv/'

app = typer.Typer()

def get_page(url: str) -> requests.Response:
    page = requests.get(url)
    if not page.ok:
      raise Exception("Error, unable to fetch " + url + " status code " + str(page.status_code))
    return page

def get_series(content: bytes, html_class: str) -> list:
  soup = BeautifulSoup(content, 'html.parser')
  series = list()
  for elem in soup.findAll('div', {'class': html_class}):
    series.append(extract_serie_name(elem.text))
  if series == list():
    raise Exception('Error, unable to find series on page content for class ' + html_class)
  return series

def extract_serie_name(serie_name : str) -> str:
  return (serie_name.rsplit(' ', 1)[0]).strip('\n')

def printseries(type: str):
  airdates = get_page(airdates_baseurl)
  series = get_series(airdates.content, 'entry ' + type + '-premiere')
  for serie in series:
    print(serie)

@app.command()
def series():
  printseries('series')

@app.command()
def season():
  printseries('season')

if __name__ == '__main__':
    app()