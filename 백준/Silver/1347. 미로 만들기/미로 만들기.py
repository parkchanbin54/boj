import sys

input = sys.stdin.readline

N = int(input())
action = input().strip()

loc_list = [(0, 0)] 
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] 
status = 2
for a in action:
    if a == 'R':
        status = (status + 1) % 4
    elif a == 'L':
        status = (status - 1) if status != 0 else 3
    else:
        x = loc_list[-1][0] + dx[status]
        y = loc_list[-1][1] + dy[status]
        loc_list.append((x, y))
        

x_sort = sorted(loc_list, key=lambda x: x[0])
y_sort = sorted(loc_list, key=lambda x: x[1])
x_min, x_max = x_sort[0][0], x_sort[-1][0]
y_min, y_max = y_sort[0][1], y_sort[-1][1]


maze = [['#' for y in range(y_min, y_max + 1)] for x in range(x_min, x_max + 1)]

for i in range(len(loc_list)):
    loc_list[i] = (loc_list[i][0] - x_min, loc_list[i][1] - y_min)


for i, j in loc_list:
    maze[i][j] = '.'

for row in maze:
    print(''.join(row))