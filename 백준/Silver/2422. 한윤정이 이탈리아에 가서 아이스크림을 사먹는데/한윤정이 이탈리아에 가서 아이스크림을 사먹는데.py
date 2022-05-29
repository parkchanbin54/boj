def sol():
    A,B = map(int,input().split())
    ice = [[False for _ in range(A)] for _ in range(A)]
    for i in range(B):
        i1, i2= map(int, input().split())
        ice[i1-1][i2-1]=True
        ice[i2-1][i1-1]=True
    result=0

    for i in range(A):
        for j in range(i+1,A):
            for k in range(j+1,A):
                if not ice[i][j] and not ice[j][k] and not ice[i][k]:
                    result+=1
    print(result)

sol()
