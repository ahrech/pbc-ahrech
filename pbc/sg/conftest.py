import pytest

from pbc.sg.connections import SshClient


@pytest.fixture(scope="module")
def ssh_client():
    client = SshClient('192.168.33.10', 'vagrant', 'vagrant')
    yield client
    client.execute('killall java')
    client.close()
