import sys
from collections import deque

def plus(a):
    return a + 32768


def check(start, con, end):
    queue = deque()
    queue.append(start)
    checked = [0] * con_n

    while queue:
        cur_x, cur_y = queue.popleft()
        if abs(cur_x - end[0]) + abs(cur_y - end[1]) <= 1000:
            return True

        for i in range(len(con)):
            if abs(cur_x - con[i][0]) + abs(cur_y - con[i][1]) <= 1000 and checked[i] == 0:
                queue.append((con[i][0], con[i][1]))
                checked[i] = 1
    return False

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    for _ in range(n):

        con_n = int(input())
        start = list(map(int,(input().split())))
        start = list(map(plus,start))

        con = list(map(int,input().split()) for _ in range(con_n))
        for i in range(con_n):
            con[i] = list(map(plus,con[i]))

        end = list(map(int,input().split()))
        end = list(map(plus,end))

        if check(start,con,end):
            print("happy")
        else:
            print("sad")