import sys
import copy

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int,input().split())
    ans = []
    pq = []
    def back_tracking():
        if sum(pq) == n:
            ans.append(copy.deepcopy(pq))
            return

        for i in range(1,4):
            if sum(pq) + i <= n:
                pq.append(i)
                back_tracking()
                pq.pop()

    back_tracking()
    answer = ""
    if len(ans) < m-1:
        print(-1)
    else:
        for k in ans[m-1]:
            answer += (str(k) + "+")
        print(answer[:-1])

