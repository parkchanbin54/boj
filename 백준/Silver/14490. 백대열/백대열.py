import sys


def gcd(a,b):
    while b != 0:
        a = a % b
        return gcd(b,a)
    return a

if __name__ == '__main__':
    input = sys.stdin.readline
    s = input().rstrip()
    a = s[:s.index(':')]
    b = s[s.index(':')+1:]

    g = 0
    if a > b:
        g = gcd(int(a),int(b))
    else:
        g = gcd(int(b),int(a))

    print(str(int(a)//g)+':'+str(int(b)//g))

