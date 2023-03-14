import sys
from collections import Counter
def sum3():
    cnt = 0

    for i in range(n):
        l, r = i+1, n-1
        while l < r:
            tmp = nums[i]+nums[l]+nums[r]
            if tmp == 0:
                if nums[l] != nums[r]:
                    cnt += counter[nums[r]]
                else:
                    cnt += r - l
                l += 1
            elif tmp > 0:
                r -= 1
            else:
                l += 1

    return cnt

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    nums = list(map(int,input().split()))

    nums.sort()
    counter = Counter(nums)
    print(sum3())