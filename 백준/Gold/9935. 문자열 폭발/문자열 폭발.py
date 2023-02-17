import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    base = list(input().rstrip())

    bomb = list(input().rstrip())
    stack = []


    for b in base:
        stack.append(b)

        if stack[-len(bomb):] == bomb:
            for _ in range(len(bomb)):
                stack.pop()

    if len(stack) == 0:
        print("FRULA")
    else:
        print(''.join(map(str,stack)))
