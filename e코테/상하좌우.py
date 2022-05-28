# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def sol():
    move = ['L', 'R', 'U', 'D']
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    x, y = 1, 1
    n = int(input())
    movelist = input().split()

    for i in movelist:
        for t in range(len(move)):
            if i == move[t]:
                nx = x + dx[t]
                ny = y + dy[t]

        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x = nx
        y = ny
    print(x, y)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol()


