import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    cnt = 1

    while True:
        tmp = input()
        if '-' in tmp:
            break
        stack = []
        count = 0
        for t in tmp:
            if t == '}':
                if not stack:
                    count += 1
                    stack.append('{')
                else:
                    stack.pop()
            else:
                stack.append(t)
        print(str(cnt)+". "+str(len(stack)//2 + count))
        cnt +=1

