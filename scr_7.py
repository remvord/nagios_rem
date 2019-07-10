import os
import re

available_spare = 100
available_spare_threshold = 'available_spare_threshold'

# команда на выполнение
command = 'echo password | sudo -S nvme smart-log /dev/nvme0n1'
# открываем канал команды читаем файл
pipe = os.popen(command)

# пробегаемся циклом по файлу на поиск соответствия значения available_spare_threshold
# извлекаем значение
for line in pipe:
    if re.search(available_spare_threshold, line):
        m = int(line.strip()[38:-1])
        if m >= available_spare*0.9:
            print('ALARM!!!')
        elif m >= available_spare*0.7:
            print('Warning!')
        else:
            print("It`s OK")





