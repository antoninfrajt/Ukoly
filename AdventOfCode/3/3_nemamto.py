from os.path import realpath, dirname, join
import itertools
import math
import re
from collections import defaultdict

with open(join(dirname(realpath(__file__)),"test.txt")) as f:
    ls = f.read().strip().split("\n")

box = list(itertools.product((-1, 0, 1), (-1, 0, 1)))
symbols = {
    (i, j)
    for i, l in enumerate(ls)
    for j, x in enumerate(l)
    if x != "." and not x.isdigit()
}
print(symbols)
print(box)

part_sum = 0
parts_by_symbol = defaultdict(list)

for i, l in enumerate(ls):
    for match in re.finditer(r"\d+", l):
        n = int(match.group(0))
        boundary = {
            (i + di, j + dj)
            for di, dj in box
            for j in range(match.start(), match.end())
        }
        if symbols & boundary:
            part_sum += n
        for symbol in symbols & boundary:
            parts_by_symbol[symbol].append(n)

# Part 1
print(part_sum)

# Part 2
print(sum(math.prod(v) for v in parts_by_symbol.values() if len(v) == 2))