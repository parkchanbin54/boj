import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    u = set()

    for _ in range(n):
        t = int(input())
        u.add(t)

    absum = set()

    for i in u:
        for j in u:
            absum.add(i+j)

    ans = {}
    for i in u:
        for j in u:
            if (i-j) in absum:
                ans[i] = (i,j,i-j)

    keys = list(ans.keys())
    keys.sort()
    print(keys[-1])
