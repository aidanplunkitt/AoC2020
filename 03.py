import math

class Slope:
    def __init__(self, right, down=1):
        self.right = right
        self.down  = down
        self.h_pos = 0
        self.v_pos = 0
        self.trees = 0

    def move(self, line):
        if self.v_pos == 0:
            if line[self.h_pos] == '#':
                self.trees += 1
            self.h_pos = (self.h_pos + self.right) % len(line)
        self.v_pos = (self.v_pos + 1) % self.down
        
slopes = [Slope(1), Slope(3), Slope(5), Slope(7), Slope(1, 2)]

with open('3.txt') as fp:
    for line in fp:
        line = line.rstrip()
        for slope in slopes:
            slope.move(line)

result = math.prod(slope.trees for slope in slopes)
print(result)