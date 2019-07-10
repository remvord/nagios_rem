import paramiko

x = 104
y = 200


def str_():
    try:
        ip = '172.30.2.'
        for i in range(x, y):
            host = (ip + str(i))

            user = 'usermc'
            psw = 'setup'
            port = 22
            command = 'df -h'

            print(host)

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

    except paramiko.ssh_exception.NoValidConnectionsError:
        print('invalid ip addresses ' + host + '\n')
        str_()


str_()
