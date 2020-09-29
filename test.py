import math
import numpy as np
import scipy as sp 
import os
import sys

path = './input.txt'

with open(path) as f:
    s = f.read()

lines = s.splitlines()



inp_list = []
ans = ''
lines.pop(len(lines)-1)

m = int(lines[len(lines)-1])
lines.pop(len(lines)-1)

for line in lines:
    sub_list = line.split(':')
    sub_list[0] = int(sub_list[0])
    inp_list.append(sub_list)
    



inp_list.sort(key = lambda x : x[0])



for elem in inp_list:
    if(m%elem[0] == 0):
        ans += elem[1]

if(ans):
    print(ans)
else:
    print(m)

