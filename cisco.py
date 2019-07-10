import time
from datetime import datetime
import paramiko

login = 'usermc'
passw = 'setup'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
file = open('device.txt', 'r')

for line in file:
    timestamps = str(datetime.now())
    print('Timestamp:', timestamps)


    def connector():
        print('Connecting to IP:' + line)
        client.connect(line, username=login, password=passw, look_for_keys=False, allow_agent=False)


    try:
        connector()
        with client.invoke_shell() as ssh:
            # ssh.send('ena\n')
            # ssh.send(passw + '\n')
            # ssh.send('terminal length 0\n')
            ssh.send('df -h\n')
            time.sleep(5)
            result = ssh.recv(200000).decode('utf-8')
            fo = open(line.strip() + '.txt', 'w')
            fo.writelines(result)
            fo.close()
    except Exception as e:
        error_log = str(e)
        print(error_log + '\n')

file.close()