"""a module that try connecting to server"""
import paramiko


command = "df"

host = "IP_ADDRESS"
username = "USER_ACCOUNT"
password = "YOUR_PASSWORD"


client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout, _stderr = client.exec_command(command)
data = _stdout.read().decode()
client.close()