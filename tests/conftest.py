import paramiko
import pytest
import time


@pytest.fixture(scope="module", autouse=True)
def start_selenium():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect('192.168.33.10', username='vagrant', password='vagrant')
    stdin, stdout, stderr = client.exec_command('pgrep java')
    pgrep = stdout.readlines()
    if len(list(pgrep)) < 2:
        print "Setting up Selenium..."
        client.exec_command('wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X')
        time.sleep(10)
        client.exec_command('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')
        time.sleep(10)
        client.exec_command(
            'java -jar selenium-server-standalone-3.8.0.jar -role node  -hub http://localhost:4444/grid/register >> log.txt 2>&1 &')
        time.sleep(10)
    else:
        print("Selenium is already running.")
    client.close()
