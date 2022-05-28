# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def sol():
    n,m=map(int,input().split())
    result = 0
    for i in range(n):
        tmp = list(map(int,input().split()))
        min_val = min(tmp)
        result=max(result,min_val)
    print(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol()


