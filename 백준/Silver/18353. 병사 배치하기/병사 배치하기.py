import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    sol = list(map(int,input().split()))

    mem = [1e9]

    for s in sol:
        if mem[-1] > s:
            mem.append(s)
        else:
            left = 0
            right = len(mem)

            while left < right:
                mid = (left + right)//2

                if mem[mid] > s:
                    left = mid + 1
                else:
                    right = mid
            mem[right] = s

    print(n- len(mem)+1)
