import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    students = list(map(int,input().split()))

    students.sort()

    ans = 1e9

    left = 0
    right = len(students)-1

    while left < right:
        tmp = students[left] + students[right]
        if ans > tmp:
            ans = tmp

        left += 1
        right -= 1

    print(ans)