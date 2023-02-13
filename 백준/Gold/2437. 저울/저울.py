import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    chu = list(map(int,input().split()))

    chu.sort()

    ans = 1

    for c in chu:
        if ans >=  c:
            ans += c

        else:
            break

    print(ans)