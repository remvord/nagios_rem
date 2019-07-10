# 1. открыть файл считать с него ip
# 2. вывести на экран или форму актуальные ip

import re
from collections import Counter
import csv


def reader(filename):
    regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    with open(filename) as f:
        log = f.read()
        ips_list = re.findall(regexp, log)

    return ips_list
    # print(ips_list)


def count(ips_list):
    return Counter(ips_list)


def write_csv(count):
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['IP', 'Freequency']
        writer.writerow(header)

        for item in count:
            writer.writerow((item, count[item]))


if __name__ == '__main__':
    write_csv(count(reader('Radm_log.htm')))
