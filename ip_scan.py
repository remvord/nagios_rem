import paramiko


ip = '172.30.2.'
for i in range(104, 150):
    host = (ip + str(i))

    user = 'usermc'
    psw = 'setup'
    port = 22
    command = 'df -h'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Подключение
    ssh.connect(hostname=host, username=user, password=psw, port=port)

    # Выполнение команды
    stdin, stdout, stderr = ssh.exec_command(command)
    # result = stdout.read() + stderr.read()
    result = stdout.readlines()
    for n in result:
        print(n.strip())
    ssh.close()