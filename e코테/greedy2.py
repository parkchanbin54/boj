# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def sol():
    n,m,k=map(int, input().split())
    data=list(map(int,input().split()))

    data.sort()
    tmp=0
    result=0
    for i in range(m):
        if tmp>=k:
            result+=data[n-2]
            tmp=0
        else:
            result+=data[n-1]
            tmp+=1

    print(result)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol()


