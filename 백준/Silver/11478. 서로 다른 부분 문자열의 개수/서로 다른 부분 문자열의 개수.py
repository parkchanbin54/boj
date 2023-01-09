import sys
if __name__ == '__main__':
    input = sys.stdin.readline
    word = input().rstrip()
    ans = set()
    for i in range(len(word)):
        for j in range(i,len(word)):
            tmp = word[i:j+1]
            ans.add(tmp)
    print(len(ans))