import pytest
from unittest.mock import patch 

from exportseries import main

def test_get_page():
  with patch('exportseries.main.requests.get') as mock_request:
    url = 'http://google.com/'
    mock_request.return_value.ok = True
    mock_request.return_value.status_code = 200
    main.get_page(url)
    mock_request.assert_called_once_with(url)

def test_get_page_raises_exception():
  with patch('exportseries.main.requests.get') as mock_request:
    with pytest.raises(Exception):
      mock_request.return_value.ok = False
      mock_request.return_value.status_code = 404
      url = 'http://google.com/'
      main.get_page(url)

def test_extract_serie_name():
  assert 'Frankie Drake Mysteries' == main.extract_serie_name('Frankie Drake Mysteries S01E01')

def test_get_series_empty():
  with pytest.raises(Exception):
    main.get_series('')

def test_get_series_find_all_elements():
  assert 1 == len(main.get_series('<html><head></head><body><div class="title">All Rise S02E04</div></body></html>'))
  assert 2 == len(main.get_series('<html><head></head><body><div class="title">All Rise S02E04</div><div class="title">Attack On Titan S04E01</div></body></html>'))

def test_get_series_extracts_series_names():
  series = main.get_series('<html><head></head><body><div class="title">All Rise S02E04</div><div class="title">Attack On Titan S04E01</div></body></html>')
  assert 2 == len(series)
  assert 'All Rise' in series
  assert 'Attack On Titan' in series