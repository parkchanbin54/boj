# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

def sol():

    n,m,k=map(int,input().split())
    arr=list(map(int,list(input().split())))
    arr.sort(reverse=True)
    i=0
    check=0
    result=0
    for _ in range(m):
        if(check<k):
            result+=arr[0]
            check+=1
        else:
            check=0
            result+=arr[1]
    print(result)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol()

