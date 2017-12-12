import pytest

from pbc.sg.connections import SshClient
from pbc.sg.sg import Grid, StartGrid


@pytest.fixture(scope="module", autouse=True)
def ssh_client():
    client = SshClient('192.168.33.10', 'vagrant', 'vagrant')
    yield client
    client.execute('killall java')
    client.close()


@pytest.fixture(scope="module", autouse=True)
def start_selenium(ssh_client):
    grid = StartGrid(Grid(ssh_client))
    grid.download()
    grid.start_hub()
    grid.add_node()
