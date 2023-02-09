import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    houses = list(map(int,input().split()))
    houses.sort()
    print(houses[(N-1)//2])