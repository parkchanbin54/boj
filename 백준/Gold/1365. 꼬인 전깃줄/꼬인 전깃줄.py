import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int,input().split()))

    mem = [0]

    for num in nums:
        if mem[-1] < num:
            mem.append(num)
        else:
            left = 0
            right = len(mem)

            while left < right:
                mid = (left + right)//2
                if mem[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            mem[right] = num

    print(n-(len(mem)-1))