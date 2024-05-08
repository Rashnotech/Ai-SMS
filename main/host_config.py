"""a module that try connecting to server"""
import paramiko
from .models import Server


command = "df"

server = Server.get_server()

host = server.ipaddress
username = server.hostname
password = server.passphrase


client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout, _stderr = client.exec_command(command)
data = _stdout.read().decode()
client.close()