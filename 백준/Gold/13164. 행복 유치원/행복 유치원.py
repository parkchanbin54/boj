import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, k = map(int,input().split())
    students = list(map(int,input().split()))

    ans = []

    for i in range(n-1):
        ans.append(students[i+1] - students[i])

    ans.sort()

    for _ in range(k-1):
        ans.pop()

    print(sum(ans))