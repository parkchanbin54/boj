import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    ans = 0

    positive = []
    negative = []

    for _ in range(N):
        tmp = int(input())
        if tmp > 1:
            positive.append(tmp)
        elif tmp == 1:
            ans += 1
        else:
            negative.append(tmp)

    positive.sort(reverse = True)
    negative.sort()

    if len(positive) % 2 == 0:
        for i in range(0,len(positive),2):
            ans += positive[i] * positive[i+1]
    else:
        for i in range(0,len(positive)-1,2):
            ans += positive[i] * positive[i+1]
        ans += positive[len(positive)-1]

    if len(negative) % 2 == 0:
        for i in range(0, len(negative),2):
            ans += negative[i] * negative[i+1]
    else:
        for i in range(0, len(negative)-1, 2):
            ans += negative[i] * negative[i+1]
        ans += negative[len(negative)-1]


    print(ans)