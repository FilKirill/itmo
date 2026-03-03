import math
import itertools

a = len(set(itertools.permutations('RRUUUBBBBUD')))
b = len(set(itertools.permutations('RRUUUBBBBRL')))
c = len(set(itertools.permutations('RRUUUBBBBBH')))
print(math.log(a + b + c, 2))
print(33 - 17)
