import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    
    tmp = list(map(str,input().rstrip()))
    check = ['U','C','P','C']

    flag = True

    for i in range(4):
        if check[i] in tmp:
            tmp = tmp[tmp.index(check[i])+1:]
        else:
            flag = False

    if flag:
        print("I love UCPC")
    else:
        print("I hate UCPC")
