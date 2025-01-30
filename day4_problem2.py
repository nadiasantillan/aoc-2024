# The Elf looks quizzically at you. Did you misunderstand the assignment?
# Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; 
# it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. 
import time

ROTATIONS = ["MMSS", "SSMM", "MSSM", "SMMS"]

lines = [line.strip() for line in open("data/day4.txt")]

start = time.time()
print(sum(1 
          for i in range(1, len(lines)-1) 
            for j in range(1, len(lines)-1)
                # M   M   # S   M   # S   S   # M   S
                #   A     #   A     #   A     #   A
                # S   S   # s   M   # M   M   # M   S
                if lines[i][j] == 'A' and 
                lines[i-1][j-1]+lines[i-1][j+1]+lines[i+1][j+1]+lines[i+1][j-1] in ROTATIONS))


print("{} seconds".format(time.time() - start))

