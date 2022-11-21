import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    for _ in range(n):
        stack = []
        tmp = []

        password = input().rstrip()

        for p in password:
            if p == '<':
                if len(stack) != 0:
                    tmp.append(stack.pop())
            elif p == '>':
                if len(tmp) != 0:
                    stack.append(tmp.pop())
            elif p == '-':
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(p)
        result = "".join(map(str,stack))
        if len(tmp) != 0:
            for _ in range (len(tmp)):
                result += tmp.pop()
        print(result)