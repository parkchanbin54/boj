import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    works = [list(map(int,input().split())) for _ in range(n)]

    works.sort(key=lambda x: - x[1])

    time = works[0][1]-works[0][0]
    flag = True

    for i in range(1,n):
        if time > works[i][1]:
            time = works[i][1] - works[i][0]
        else:
            time -= works[i][0]

    print (time if time >= 0 else -1)



