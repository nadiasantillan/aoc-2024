ROTATIONS = ["MMSS", "SSMM", "MSSM", "SMMS"]

lines = [line.strip() for line in open("data/day4.txt")]
print(sum(1 
          for i in range(1, len(lines)-1) 
            for j in range(1, len(lines)-1) 
                if lines[i][j] == 'A' and 
                lines[i-1][j-1]+lines[i-1][j+1]+lines[i+1][j+1]+lines[i+1][j-1] in ROTATIONS))




