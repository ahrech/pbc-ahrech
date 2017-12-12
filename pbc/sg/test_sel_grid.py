import pytest


@pytest.mark.selenium
def test_sg_sm(start_selenium, ssh_client):
    assert len(list(ssh_client.execute('pgrep java').readlines())) == 2

@pytest.mark.selenium
def test_log_no_errors(start_selenium, ssh_client):
    assert len(list(ssh_client.execute('grep Error log.txt').readlines())) == 0
