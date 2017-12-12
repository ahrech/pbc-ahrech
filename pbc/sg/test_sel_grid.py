import pytest

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
