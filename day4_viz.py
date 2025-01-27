import json

XMAS = "XMAS"
SAMX = "SAMX"
XMAS_LENGTH = len(XMAS)

class Map:
    def __init__(self, filename=None, lines=None):
        if filename:
            self.lines = [line.strip() for line in open(filename)]
        elif lines:
            self.lines = lines

    def dimensions(self):
        return (len(self.lines), len(self.lines[0]))

    def diagonals(self):
        res = []
        l, w = self.dimensions()
        for i in range(l):
            dur = []
            dul = []
            dll = []
            dlr = []
            for j in range(w - i):
                dur.append((self.lines[j][j+i], j, j+i))
                dul.append((self.lines[j][w-j-i-1], j, w-j-i-1))
                if i > 0:
                    dll.append((self.lines[i+j][j], i+j, j))
                    dlr.append((self.lines[i+j][w-j-1], i+j, w-j-1))
            res.extend([dur, dul])
            if i > 0:
                res.extend([dll, dlr])
        return res
    
    def verticals(self):
        l, w = self.dimensions()
        res = []
        for c in range(w):
            col = []
            for i in range(l):
                col.append((self.lines[i][c], i, c))
            res.append(col)
        return res
    
    def horizontals(self):
        l, w = self.dimensions()
        res = []
        for i in range(l):
            line = []
            for c in range(l):
                line.append((self.lines[i][c], i, c))
            res.append(line)
        return res
    
class Day4Problem1:
    def __init__(self, filename=None, lines=None):
        self.map = Map(filename=filename, lines=lines)

    def find(self, lines, term):
        matches = []
        for i, linemeta in enumerate(lines):
            line = "".join(m[0] for m in linemeta)
            j = line.find(term)
            while j > -1:
                matches.append((i, j, XMAS_LENGTH))
                j = line.find(term, j + XMAS_LENGTH)
        return matches
    
    def solve1(self):
        res = {}
        h = self.map.horizontals()
        d = self.map.diagonals()
        v = self.map.verticals()
        res["horizontal"] = self.find(h, XMAS) + self.find(h, SAMX)
        res["diagonal"] = self.find(d, XMAS) + self.find(d, SAMX)
        res["vertical"] = self.find(v, XMAS) + self.find(v, SAMX)

        return res
    
    def json(self, filename="data/day4.json"):
        with open(filename, "wt") as f:
            json.dump({
                "length": self.map.dimensions()[0],
                "width": self.map.dimensions()[1],
                "horizontal": self.map.horizontals(),
                "vertical": self.map.verticals(),
                "diagonal": self.map.diagonals(),
                "solution1": self.solve1(),
                "solution2": self.solve2()}, f)
    
    def solve2(self):
        s = 0
        lines = self.map.horizontals()
        stars = []
        for i in range(1, len(lines)-1):
            for j in range(1, len(lines)-1):
                if lines[i][j][0] == 'A':
                    if lines[i-1][j-1][0]+lines[i-1][j+1][0]+lines[i+1][j+1][0]+lines[i+1][j-1][0] in ["MMSS", "SSMM", "MSSM", "SMMS"] :
                        s+=1
                        stars.append([(i, j), (i-1, j-1), (i-1, j+1), (i+1, j+1), (i+1, j-1)])
        return dict(stars=stars)


problem = Day4Problem1(filename="data/day4-sample.txt")
problem.json(filename="data/day4-sample.json")


