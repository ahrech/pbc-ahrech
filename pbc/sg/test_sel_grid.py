import pytest
import requests
from requests import RequestException

from pbc.sg.sg import SmartGrid, Grid
from pbc.sg.utils import find_occurrences


@pytest.mark.selenium
def test_sg_sm(ssh_client):
    grid = SmartGrid(Grid(ssh_client))
    grid.download()
    grid.start_hub()
    grid.add_node()
    assert len(list(ssh_client.execute('pgrep java').readlines())) == 2


@pytest.mark.selenium
def test_log_no_errors(ssh_client):
    grid = SmartGrid(Grid(ssh_client))
    grid.download()
    grid.start_hub()
    grid.add_node()
    assert len(list(ssh_client.execute('grep Error log.txt').readlines())) == 0


@pytest.mark.firefox_sessions
def test_sessions_count(ssh_client, firefox):
    grid = SmartGrid(Grid(ssh_client))
    grid.download()
    grid.start_hub()
    grid.add_node()
    try:
        firefox.get('http://192.168.33.10:4444/grid/console')
        elem = firefox.find_elements_by_xpath(
            '//*[@id="left-column"]/div/div[2]/div[1]/p[2]/img[contains(@src, "firefox")]')
        assert len(elem) == 5
    except Exception as a:
        print 'Page failed to load. Error: {}'.format(a.message)
        raise a


@pytest.mark.firefox_sessions
def test_sessions_count_requests(ssh_client):
    grid = SmartGrid(Grid(ssh_client))
    grid.download()
    grid.start_hub()
    grid.add_node()
    try:
        r = requests.get('http://192.168.33.10:4444/grid/console')
        assert r.status_code == 200
        result = find_occurrences(r.text, 'firefox.png')
        assert len(result) == 5
    except RequestException as a:
        print 'Request failed.'
        raise a
