import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, m = map(int,input().split())
        students = []

        for _ in range(m):
            a,b = map(int,input().split())
            students.append((a,b))

        students.sort(key = lambda x : x[1])

        visited = [False] * (n+1)
        ans = 0
        for start, end in students:
            for i in range(start,end+1):
                if not visited[i]:
                    ans += 1
                    visited[i] = True
                    break
        print(ans)