import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    q = []
    for i in range(8):
        tmp = int(input())
        q.append((tmp, i+1))

    q.sort()
    a = []
    ans_list = ""
    ans = 0
    for i in range(7,2,-1):
        ans += q[i][0]
        a.append(q[i][1])

    a.sort()

    print(ans)
    for i in a:
        ans_list += str(i) + ' '
    print(ans_list)