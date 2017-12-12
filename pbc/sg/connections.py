import paramiko


class SshClient:
    def __init__(self, ip, user, pasw):
        print 'Opening SSH connection for a user {}.'.format(user)
        self._ip = ip
        self._user = user
        self._pasw = pasw
        self._connection = paramiko.SSHClient()
        self._connection.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self._connection.connect(self._ip, username=self._user, password=self._pasw)

    def execute(self, command):
        print '[{u}:{p} -> {c}]'.format(u=self._user, p=self._pasw, c=command)
        stdin, stdout, stderr = self._connection.exec_command(command)
        return stdout

    def close(self):
        print 'Closing [{u}:{p}]'.format(u=self._user, p=self._pasw)
        self._connection.close()
