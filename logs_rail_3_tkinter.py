import re
import threading
from tkinter import *
import time

window = Tk()
window.title("How is connect")
window.geometry('220x100')


def my_script():
    f = open('Radm_log.htm', 'r')
    Count = f.readlines()
    S1 = 'Remote Screen connection'
    S2 = 'connection closed'
    regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    for i in Count:
        if i.count(S1) == 1:
            x = re.findall(regexp, i)
        if i.count(S2) == 1:
            y = re.findall(regexp, i)

    g = {'172.30.2.242': 'Игорь Щенев', '172.30.2.240': 'Булатов Всеволод', '172.30.2.130': 'Ольга Байбородова',
         '172.30.2.154': 'Юра Четайкин', '172.30.2.234': 'Андрей Хлыста', '172.30.2.212': 'Сергей Прохоров',
         '172.30.2.218': 'DMZ Gateway', '172.30.2.100': 'Антон Васильев', '172.30.2.161': 'Владимир Байбичук',
         '172.30.2.169': '???', '172.16.255.46': 'Алексей Байбородов', '172.16.255.29': 'Владимир Байбичук(vpn)',
         '172.16.255.56': 'VPN', '172.30.2.102': 'Victor'}
    v = list(set(x + y))

    for d in v:
        for key in g:
            if key == d:
                Label(window, text="Connect now " + g.get(key)).grid(column=0, row=0)


threading.Timer(1, my_script).start()
time.sleep(2)
print('start')
my_script()
window.mainloop()

