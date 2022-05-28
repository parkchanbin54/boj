# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def sol():
    place = input()
    row = int(place[1])
    col = int(ord(place[0])) - int(ord('a'))+1

    steps=[(-2,-1),(2,-1),(2,1),(-2,1),(1,2),(1,-2),(-1,2),(-1,-2)]

    result=0
    for step in steps:
        next_row = row + step[0]
        next_column = col + step[1]
        if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
            result+=1
    print(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol()


