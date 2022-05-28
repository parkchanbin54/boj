# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def sol():
    n=1260
    count=0

    coin_types=[500,100,50,10]
    for coins in coin_types:
        count+=n//coins
        n%coins
    print(count)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol()

