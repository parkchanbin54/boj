import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    for i in range(n):
        n, m  = map(int,input().split())
        days = list(map(int,input().split()))

        mem = [-1]

        for day in days:
            if mem[-1] < day:
                mem.append(day)

            else:
                left = 0
                right = len(mem)

                while left < right:
                    mid = (left + right)//2

                    if mem[mid] < day:
                        left = mid + 1
                    else:
                        right = mid

                mem[right] = day

        print("Case #"+str(i+1))
        print(1 if len(mem)-1 >= m else 0)