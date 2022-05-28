# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def sol():
    n = int(input())
    result=0
    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i)+str(j)+str(k):
                    result+=1
    print(result)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol()


