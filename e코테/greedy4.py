# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def sol():
    n,k = map(int,input().split())
    result = 0
    while n>=k:
        if n%k==0:
            n=n/k
            result+=1
        else:
            n-=1
            result+=1
    print(result)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol()


