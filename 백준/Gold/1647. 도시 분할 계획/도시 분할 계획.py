import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N, E = map(int,input().split())
    Vroot = [i for i in range(N+1)]
    Elist = []

    for _ in range(E):
        Elist.append(list(map(int,input().split())))

    Elist.sort(key = lambda x : x[2])

    def find(x):
        if x != Vroot[x]:
            Vroot[x] = find(Vroot[x])
        return Vroot[x]


    answer = 0
    selected = []
    for s, e, w in Elist:
        sRoot = find(s)
        eRoot = find(e)
        if sRoot != eRoot:
            if sRoot > eRoot:
                Vroot[sRoot] = eRoot
            else:
                Vroot[eRoot] = sRoot
            selected.append(w)
            answer += w

    print(answer - selected.pop())