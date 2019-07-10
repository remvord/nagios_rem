import subprocess
import re

result = subprocess.run(['sudo', 'nvme', 'smart-log', '/dev/nvme0'], stdout=subprocess.PIPE).stdout.decode()

avail_spare = re.search('available_spare.*: (\d+)%', result).group(1)
avail_spare_threshold = re.search('available_spare_threshold.*: (\d+)%', result).group(1)

if int(avail_spare_threshold) >= int(avail_spare) * 0.9:
    print('ALARM!!!')
elif int(avail_spare_threshold) >= int(avail_spare) * 0.7:
    print('Warning!')
else:
    print("It`s OK")