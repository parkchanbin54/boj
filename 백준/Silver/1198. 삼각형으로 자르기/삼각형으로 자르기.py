from itertools import combinations
import sys


def triangle_area(x, y, z):
    return abs((x[0]*y[1]+y[0]*z[1]+z[0]*x[1]-x[1]*y[0]-y[1]*z[0]-z[1]*x[0]))/2


jum = []
max_area = []
a = []
inp = sys.stdin.readline()

for i in range(int(inp)):
    inpp = sys.stdin.readline()
    jum.append(list(map(int, inpp.split())))

jum_list = list(combinations(jum, 3))
for k in range(len(jum_list)):
    max_area.append(triangle_area(jum_list[k][0], jum_list[k][1], jum_list[k][2]))
print(max(max_area))