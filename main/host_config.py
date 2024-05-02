"""a module that try connecting to server"""
from paramiko import SSHClient


client = SSHClient()
client.load_system_host_keys()
client.connect()

stdin, stdout, stderr = client.exec_command('ls -l')