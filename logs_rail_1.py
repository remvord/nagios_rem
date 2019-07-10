import re


#
#
#
# # for i in f:
# #     if re.findall('Remote Screen connection', i):
# #         regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
# f = open('Radm_log.htm', 'r')
# regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
#
# with f as i:
#     log = i.read()
#     ips_list = re.findall(regexp, log)
# print(ips_list)

# ignore = ['Remote', 'Screen']
# regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
# Count = regexp.count()
#
# with open('Radm_log.htm', 'r') as f:
#     for line in f.readlines():
#         if not (set(ignore) & set(line.split())):
#             print(re.findall(regexp, line), end="")

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


g = {'172.30.2.129': 'Юра', '172.30.2.175': 'Виктор', '172.30.2.212': 'Байбочук', '172.30.2.122': 'Серега'}
v = list(set(x + y))

for d in v:
    for key in g:
        if key == d:
            print('Sessions IP - ' + g.get(key))
