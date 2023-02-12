import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n, l = map(int, input().split())
    fruits = list(map(int,input().split()))

    fruits.sort()
    ans = 0

    for i in range(n):
        if l + i + 1 <= fruits[i]:
            break
        ans = l + i + 1

    print(ans)