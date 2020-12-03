import re

from utils import datapath


lines = []

with open(datapath('aoc2.txt')) as f:
    for line in f.readlines():
        line = line.strip()
        pattern = re.compile('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')
        m = pattern.match(line)
        lines.append([m.group(i) for i in range(1, 5)])

total = 0
for line in lines:
    lower, upper, c, s = line
    if int(lower) <= s.count(c) <= int(upper):
        total += 1

print(total)
