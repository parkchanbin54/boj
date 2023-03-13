import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        records = list(map(int,input().split()))

        k = int(input())
        tests = list(map(int,input().split()))
        for i in range(k):
            tests[i] = (tests[i],i)
        records.sort()
        tests.sort(reverse = True)

        left = 0
        right = k - 1
        ans = [0] * k
        while left < n and right >= 0:
            tmp = records[left] - tests[right][0]
            if tmp == 0:
                ans[tests[right][1]] = 1
                right -= 1

            elif tmp > 0:
                right -= 1
            else:
                left += 1

        for a in ans:
            print(a)



