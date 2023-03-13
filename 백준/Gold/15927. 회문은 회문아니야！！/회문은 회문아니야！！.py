import sys

def sol():
    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] != s[end]:
            return len(s)
        end -= 1
        start += 1

    start = 0
    end = len(s) - 2

    while start < end:
        if s[start] != s[end]:
            return len(s) -1
        end -= 1
        start += 1

    return -1


if __name__ == '__main__':
    input = sys.stdin.readline

    s = list(input().rstrip())

    print(sol())