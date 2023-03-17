import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    check = input().rstrip()
    ind = check.index('*')
    start, end = check[:ind], check[ind+1:]

    for _ in range(n):
        s = input().rstrip()
        if len(s) < len(start) + len(end):
            print("NE")
        else:
            if s[:len(start)] == start and s[-len(end):] == end:
                print("DA")
            else:
                print("NE")

