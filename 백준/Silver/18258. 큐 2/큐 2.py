from sys import stdin
input()
s, com= [], stdin.readlines()
cnt = 0
for x in com:
    c = x.split()
    if c[0] == "push":
        s.append(c[1])
    elif c[0] == 'pop':
        if len(s) > cnt:
            print(s[cnt])
            cnt += 1
        else: print(-1)
    elif c[0] == 'size':
        print(len(s)-cnt)
    elif c[0] == 'empty':
        if len(s) == cnt :
            print(1)
            cnt = 0
            s = []
        else: print(0)
    elif c[0] == 'front':
        if len(s) > cnt: print(s[cnt])
        else: print(-1)
    elif c[0] == 'back':
        if len(s) > cnt: print(s[-1])
        else: print(-1)