import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        s = list(input().rstrip())
        left = 0
        right = len(s) - 1
        check = False
        flag = False

        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1
        if left < right:
            left = [left, left +1]
            right = [right-1 , right]
            flag = False
            for i in range(2):
                while left[i] <= right[i]:
                    if s[left[i]] != s[right[i]]:
                        break
                    left[i] += 1
                    right[i] -= 1

                if left[i] > right[i]:
                    flag = True

            if flag:
                print(1)
            else:
                print(2)
        else:
            print(0)
