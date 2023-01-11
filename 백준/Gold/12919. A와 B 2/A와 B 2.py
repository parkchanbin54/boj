import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    S = list(input().rstrip())
    T = list(input().rstrip())

    def back_tracking(t):
        if t == S:
            print(1)
            sys.exit()
        if len(t) == 0:
            return 0
        if t[-1] == 'A':
            back_tracking(t[:-1])
        if t[0] == 'B':
            back_tracking(t[1:][::-1])


    back_tracking(T)
    print(0)