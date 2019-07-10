import os
import re
import sys

const = 100
percentage_used = 'percentage_used'

for line in str(os.system('echo remVord41 | sudo -S nvme smart-log /dev/nvme0n1')):
    for i in line:
        print(sys.stdout.write(i))
    if re.search(percentage_used, line):
        m = int(line.strip()[38:-1])
        if m >= const * 0.9:
            print('ALARM!!!')
        elif m >= const * 0.7:
            print('Warning!')
        else:
            print("It`s OK")


