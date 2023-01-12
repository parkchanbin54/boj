import sys


if __name__ == '__main__':
    input = sys.stdin.readline

    word = list(input().rstrip())
    ans = ""
    stack = []
    flag = False
    for w in word:
        if flag and w != ' ':
            ans += w

        if w == '<' or w == ' ':
            if w == '<':
                flag = True
            stack.reverse()
            ans += ''.join(s for s in stack)+w
            stack = []

        elif w == '>':
            flag = False

        else:
            if not flag:
                stack.append(w)

    if stack:
        stack.reverse()
        ans += ''.join(s for s in stack) + ' '

    print(ans)