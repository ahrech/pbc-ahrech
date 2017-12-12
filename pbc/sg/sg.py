import time
from abc import ABCMeta, abstractmethod


class BaseGrid:
    __metaclass__ = ABCMeta

    @abstractmethod
    def start_hub(self):
        pass

    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def add_node(self):
        pass


class Grid(BaseGrid):
    def __init__(self, ssh_client):
        self._client = ssh_client

    def download(self):
        print 'Download'
        stdout = self._client.execute('wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X')
        count = 0
        while count < 100:
            if stdout.channel.exit_status_ready():
                return
            time.sleep(1)
            count += 1
        raise Exception('File was not loaded')

    def start_hub(self):
        print 'Start hub'
        self._client.execute('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')

    def add_node(self):
        print 'Add node'
        self._client.execute(
            'java -jar selenium-server-standalone-3.8.0.jar -role node  -hub http://localhost:4444/grid/register >> log.txt 2>&1 &')

    def is_downloaded(self):
        stdout = self._client.execute('test -f selenium-server-standalone-3.8.0.jar && echo yes')
        if 'yes' in str(stdout.readlines()):
            print 'The file already exists.'
            return True
        else:
            return False

    def is_running(self):
        stdout = self._client.execute('pgrep java')
        pgrep = stdout.readlines()
        if len(list(pgrep)) < 2:
            return False
        else:
            print("Selenium is already running.")


class StartGrid(BaseGrid):
    def __init__(self, grid):
        self._g = grid

    def download(self):
        if not self._g.is_downloaded():
            self._g.download()

    def start_hub(self):
        if not self._g.is_running():
            self._g.start_hub()

    def add_node(self):
        if not self._g.is_running():
            self._g.add_node()
