from utils import datapath

with open(datapath('aoc1.txt')) as f:
    nums = f.read().splitlines()

nums = set(map(int, nums))

for i in nums:
    if 2020 - i in nums:
        print(i * (2020 - i))
        break
