import os
import re

available_spare = 100
available_spare_threshold = 'available_spare_threshold'

myCmd = 'echo remVord41 | sudo -S nvme smart-log /dev/nvme0n1 > out.txt'
os.system(myCmd)

f = open('out.txt', 'r')

for line in f:
    if re.search(available_spare_threshold, line):
        m = int(line.strip()[38:-1])
        if m >= available_spare*0.9:
            print('ALARM!!!')
        elif m >= available_spare*0.7:
            print('Warning!')
        else:
            print("It`s OK")

print('======================')
f1 = open('out.txt', 'r')
for line1 in f1:
    print(line1.strip())

f.close()





