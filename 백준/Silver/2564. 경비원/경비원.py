import sys


width, height = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline().strip())
store = list()

def calcDist(dir,dist):
    if dir == 1:
        return dist
    elif dir == 2:
        return width + height + (width - dist)
    elif dir == 3:
        return width + height + width + (height - dist)
    else:
        return width + dist

for _ in range(n+1):
    if _ == n:
        direction, distance = map(int,sys.stdin.readline().split())
    else:
        store.append(list(map(int,sys.stdin.readline().split())))

total = 0
dist1 = calcDist(direction, distance)
for i in range(n):
    dist2 = calcDist(store[i][0], store[i][1])
    path1 = abs(dist1 - dist2)
    path2 = 2 * width + 2 * height - path1
    total += path1 if path1 < path2 else path2

print(total)