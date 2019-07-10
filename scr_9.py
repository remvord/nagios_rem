import subprocess
import re

result = subprocess.run(['sudo', 'nvme', 'smart-log', '/dev/nvme0n1'], stdout=subprocess.PIPE).stdout.decode()
percentage_used = re.search('percentage_used.*: (\d+)%', result).group(1)

if int(percentage_used) >= 90:
    print('ALARM!!!')
elif int(percentage_used) >= 70:
    print('Warning!')
else:
    print("It`s OK")