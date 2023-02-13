import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    while True:
        n = input()
        if not n:
            break
        n = int(n)
        nums = list(map(int,input().split()))

        mem = [-1]

        for num in nums:
            if mem[-1] < num:
                mem.append(num)

            else:
                left = 0
                right = len(mem)

                while left < right:
                    mid = (left + right) // 2

                    if mem[mid] < num:
                        left = mid + 1
                    else:
                        right = mid
                mem[right] = num

        print(len(mem)-1)

