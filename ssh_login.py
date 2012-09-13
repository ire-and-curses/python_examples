#!/usr/bin/env python

'''
ssh.py - Example usage of the paramiko library for ssh control

Author: Eric Saunders
November 2010
'''

from paramiko import SSHClient, RSAKey
from getpass import getpass
from time import sleep
import os.path

def get_credentials(path):
    credentials = {}
    path_to_creds = os.path.expanduser(path)
    auth_fh = open(path_to_creds, 'r')
    for line in auth_fh:
        if line.strip().startswith('#'):
            continue

        print "line", line

        key, _, value = line.split()

        credentials[key] = value

    auth_fh.close()
    return credentials

credentials = get_credentials('~/credentials/paramiko_example.pwd')
remote_host = credentials['remote_host']
user_name   = credentials['user_name']

password = getpass('Enter password for %s at %s: ' % (user_name, remote_host))

client = SSHClient()

client.load_system_host_keys()

# Connect using a password
#client.connect(hostname=remote_host, username=user_name, password=password)

# Connect using ssh key
private_key_file = os.path.expanduser('~/.ssh/id_rsa')
client.connect(hostname=remote_host, username=user_name,
               password=password, key_filename=private_key_file)

#stdin, stdout, stderr = client.exec_command('ls -l')
cmd = '''python -c 'print "hello world"' '''
stdin, stdout, stderr = client.exec_command(cmd)
sleep(1)
client.close()

print "stdout was:"
for line in stdout:
    print line

print "stderr was:"
for line in stderr:
    print line
