import sys

def back_tracking(idx):
    global ans
    if l <= sum(tmp) <= r and len(tmp) >= 2:
        if max(tmp) - min(tmp) >= x:
            ans += 1

    if len(tmp) == n:
        return

    for i in range(idx,n):
        tmp.append(problems[i])
        back_tracking(i+1)
        tmp.pop()

if __name__ == '__main__':
    input = sys.stdin.readline

    n,l,r,x = map(int,input().split())

    problems = list(map(int,input().split()))
    ans = 0
    tmp = []

    back_tracking(0)

    print(ans)