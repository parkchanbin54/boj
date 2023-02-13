import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    tmp = input().rstrip()

    stack = []
    ppap = ['P','P','A','P']
    for t in tmp:
        stack.append(t)
        if stack[-4:] == ppap:
            for _ in range(4):
                stack.pop()
            stack.append('P')
    if stack == ppap or stack == ['P']:
        print("PPAP")
    else:
        print("NP")
