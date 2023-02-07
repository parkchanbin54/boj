import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    t = int(input())

    for i in range(t):
        n, k = map(int,input().split())
        files = list(map(int,input().split()))

        mem = [0]

        for file in files:
            if mem[-1] < file:
                mem.append(file)
            else:
                left = 0
                right = len(mem)
                while left < right:
                    mid = (left + right)//2
                    if mem[mid] < file:
                        left = mid + 1
                    else:
                        right = mid

                mem[right] = file
        print("Case #" + str(i + 1))
        if len(mem) > k:
            print(1)
        else:
            print(0)
