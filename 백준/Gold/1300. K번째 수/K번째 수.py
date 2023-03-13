import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    k = int(input())

    start , end = 1, k

    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for i in range(1,n+1):
            temp += min(mid//i , n)
        if temp >= k:
            answer = mid
            end = mid -1
        else:
            start = mid + 1
    print(answer)
