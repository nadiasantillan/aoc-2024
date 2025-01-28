import re
import time

def find_horizontal(lines):
    s = 0
    for line in lines:
        s += len(re.findall("XMAS", line)) + len(re.findall("XMAS", line[::-1]))
    return s

def find_vertical(lines):
    return find_horizontal(["".join(lines[j][i] for j in range(len(lines))) for i in range(len(lines))])

def diagonals(lines):
    return (["".join(lines[j][i+j] for j in range(len(lines)-i)) for i in range(len(lines))] +
        ["".join(lines[i+j][j] for j in range(len(lines)-i)) for i in range(1, len(lines))])

def find_diagonals(lines):
    rlines =[line[::-1] for line in lines]
    return find_horizontal(diagonals(lines)+diagonals(rlines))


lines = [line.strip() for line in open("data/day4.txt")]

l = len(lines[0])
start = time.time()
print(find_horizontal(lines) + find_vertical(lines)+ find_diagonals(lines))
print("{} seconds".format(time.time() - start))



