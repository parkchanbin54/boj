import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    for _ in range(n):
        k = int(input())

        woods = list(map(int,input().split()))
        woods.sort()

        result = 0

        for i in range(2,k):
            result = max(result, abs(woods[i-2] - woods[i]))
            
        print(result)