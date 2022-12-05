if __name__ == '__main__':
    while True:
        voca = []
        n = int(input())
        if n == 0:
            quit()
        for i in range(n):
            voca.append(input())
        voca.sort(key=str.lower)
        print(voca[0])