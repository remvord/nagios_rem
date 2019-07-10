import paramiko
import time

for num in range(223, 224):
    host = "172.30.2." + str(num)

    try:
        user = 'remvord'
        psw = '123'
        port = 22

        # exitcommand = 'sudo usermod -G sudo usermc'
        command = 'sudo su'
        command1 = 'sudo useradd -m -G adm,sudo -s /bin/bash remvord'
        command2 = 'echo "remvord  ALL=(ALL:ALL)   NOPASSWD:ALL" | sudo tee --append /etc/sudoers'
        command3 = 'sudo mkdir /home/remvord/.ssh'
        command3_1 = 'sudo chmod 0700 /home/remvord/.ssh'
        command4 = 'sudo touch /home/remvord/.ssh/authorized_keys'
        command4_1 = 'sudo chmod 0644 /home/remvord/.ssh/authorized_keys'
        command4_2 = 'sudo chown -R remvord:remvord /home/remvord/.ssh/'
        command5 = 'echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDObwVf1Eln+F6X1G3gb3z7H5/MLN2AFVgk5d0KRzjitP/Zj+p09xGH11Trp+s0hwrZPRkvEf3ZTXkhVA1iMUNTX+pnML3RsRNLXqavZGBucXiggDMdtLAsagGJsuP1DKyJUjiJy3cQR8InL7MBAdmCFYtCBNnS6On51neJCEDOmYHwWBQSm3JERotve1lEpMqXFKh8AYq8ybS4TAOVegGGvSLa+GLsm0SMyJpJITT2dfIuaUBphXOu2/N7g16oFwMSkKKfpL5TtOF3GTN0RTea0pvA5e5Rthe+IMQHwImmVuNw9MOyHfG0YUh/I3GTbliXWUsEjxj6dpZF4rdk7M9T remvord@ws048" | sudo tee --append /home/remvord/.ssh/authorized_keys'

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=psw, port=port, timeout=5)

        stdin, stdout, stderr = ssh.exec_command(command)
        time.sleep(2)
        stdin1, stdout1, stderr1 = ssh.exec_command(command1)
        time.sleep(2)
        stdin2, stdout2, stderr2 = ssh.exec_command(command2)
        time.sleep(2)
        stdin3, stdout3, stderr3 = ssh.exec_command(command3)
        time.sleep(2)
        stdin3_1, stdout3_1, stderr3_1 = ssh.exec_command(command3_1)
        time.sleep(2)
        stdin4, stdout4, stderr4 = ssh.exec_command(command4)
        time.sleep(2)
        stdin4_1, stdout4_1, stderr4_1 = ssh.exec_command(command4_1)
        time.sleep(2)
        stdin4_2, stdout4_2, stderr4_2 = ssh.exec_command(command4_2)
        time.sleep(2)
        stdin5, stdout5, stderr5 = ssh.exec_command(command5)
        time.sleep(2)
        print(host + ' OK' + '\n')

        result = stdout1.readlines()
        for n in result:
            print(n.strip())
        ssh.close()

    except paramiko.ssh_exception.NoValidConnectionsError:
        print('Not connect ip addr ' + host + '\n')

    except paramiko.ssh_exception.AuthenticationException:
        print('Not user/passw usermc ' + host + '\n')

    except paramiko.ssh_exception.SSHException:
        print('ssh_error ' + host + '\n')

    except paramiko.ssh_exception.socket.timeout:
        print('limit timeout ' + host + '\n')