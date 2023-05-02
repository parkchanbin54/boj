import sys
tmp = []
idxs = []


def back_tracking():
    global ans

    if len(tmp) == len(a):
        t = int(''.join(tmp))
        if t < int(b) and len(str(t)) == len(a) :
            ans = max(ans, t)

    for i in range(len(a_list)):
        if i not in idxs:
            tmp.append(a[i])
            idxs.append(i)
            back_tracking()
            tmp.pop()
            idxs.pop()



if __name__ == "__main__":
    input = sys.stdin.readline

    a, b = map(str,input().split())
    ans = 0
    a_list = list(str(a))

    a_list.sort(reverse = True)

    back_tracking()
    if ans == 0:
        print(-1)
    else:
        print(ans)