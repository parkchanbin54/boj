import sys
from collections import defaultdict

def back_tracking(idx,l,dict):

    if len(tmp)!= 0:
        dict[sum(tmp)] += 1

    for i in range(idx,len(l)):
        tmp.append(l[i])
        back_tracking(i+1,l,dict)
        tmp.pop()


if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int,input().split())
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)

    nums = list(map(int,input().split()))

    nums1 = nums[:n//2]
    nums2 = nums[n//2:]

    tmp = []
    back_tracking(0,nums1,dict1)
    back_tracking(0,nums2,dict2)
    ans = 0

    for s in dict1:
        if m - s in dict2:
            ans += dict2[m-s] * dict1[s]

    ans += dict1[m] + dict2[m]

    print(ans)
