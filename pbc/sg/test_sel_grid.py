import pytest
from selenium import webdriver
from pbc.sg.sg import SmartGrid, Grid


@pytest.mark.selenium
def test_sg_sm(ssh_client):
    grid = SmartGrid(Grid(ssh_client))
    grid.download()
    grid.start_hub()
    grid.add_node()
    assert len(list(ssh_client.execute('pgrep java').readlines())) == 2


@pytest.mark.selenium
def test_log_no_errors(ssh_client):
    assert len(list(ssh_client.execute('grep Error log.txt').readlines())) == 0


@pytest.mark.selenium
def test_sessions_count():
    driver = webdriver.Firefox()
    driver.get('http://192.168.33.10:4444/grid/console')
    elem = driver.find_elements_by_xpath('//*[@id="left-column"]/div/div[2]/div[1]/p[2]/img[contains(@src, "firefox")]')
    assert len(elem) == 5
    driver.close()
