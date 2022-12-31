import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    for _ in range(n):

        min_ans = 0
        max_ans = 0
        stick, ant_num = map(int,input().split())
        ants = [int(input().rstrip()) for _ in range(ant_num)]

        for ant in ants:
            min_ans = max(min_ans,min(ant, stick - ant))
            max_ans = max(max_ans, ant, stick-ant)


        print(min_ans, max_ans)
