# A small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word 
# search. She only has to find one word: XMAS.
# This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words.
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
    #   0 1 2 3 4 5 6 7 8 9   #   0 1 2 3 4 5 6 7 8 9   #   0 1 2 3 4 5 6 7 8 9   #   0 1 2 3 4 5 6 7 8 9  
    # 0 x                     # 0   x                   # 0                       # 0       
    # 1   x                   # 1     x                 # 1 m                     # 1                   m                   
    # 2     x                 # 2       x               # 2   a                   # 2                 a             
    # 3       x               # 3         x             # 3     c                 # 3               c               
    # 4         x             # 4           x           # 4       a               # 4             a             
    # 5           x           # 5             x         # 5         d             # 5           d        
    # 6             x         # 6               x       # 6           a           # 6         a         
    # 7               x       # 7                 x     # 7             m         # 7       m
    # 8                 x     # 8                   x   # 8               i       # 8     i
    # 9                   x   # 9                       # 9                 a     # 9   a   
    # r 0 1 2 3 4 5 6 7 8 9   # r   0 1 2 3 4 5 6 7 8   # r 1 2 3 4 5 6 7 8 9     # r   9 8 7 6 5 4 3 2 1
    # c 0 1 2 3 4 5 6 7 8 9   # c   1 2 3 4 5 6 7 8 9   # c 0 1 2 3 4 5 6 7 8     # c   1 2 3 4 5 6 7 8 9
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



