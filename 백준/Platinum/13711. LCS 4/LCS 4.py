import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    n1 = list(map(int,input().split()))
    n2 = list(map(int,input().split()))

    dn1 = dict().fromkeys([i for i in range(n+1)],-1)
    dn2 = dict().fromkeys([i for i in range(n+1)],-1)


    for i in range(n):
        dn1[n1[i]] = i
        dn2[n2[i]] = i


    k = []
    for i in range(n):
        k.append(dn2[n1[i]])

    def LCS_up(nn):
        mem = [-1]
        for i in nn:
            if mem[-1] < i:
                mem.append(i)
            else:
                left = 0
                right = len(mem)
                while left < right:
                    mid = (left + right) // 2
                    if mem[mid] < i:
                        left = mid + 1
                    else:
                        right = mid
                mem[right] = i
        return len(mem)-1

    print(LCS_up(k))
