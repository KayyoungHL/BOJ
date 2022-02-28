import sys
"""
n = 1
0,0 = 00 = 0
0,1 = 01 = 1
1,0 = 10 = 2
1,1 = 11 = 3

n = 2
0,2 => 00, 10 => 0,1 0,0 => 100 = 4
0,3 => 00, 11 => 0,1 0,1 => 101 = 5
1,2 => 01, 10 => 0,1 1,0 => 110 = 6
1,3 => 01, 11 => 0,1 1,1 => 111 = 7

2,2 => 10, 10 => 1,1 0,0 => 1100 = 12
2,3 => 10, 11 => 1,1 0,1 => 1101 = 13
3,2 => 11, 10 => 1,1 1,0 => 1110 = 14
3,3 => 11, 11 => 1,1 1,1 => 1111 = 15

n = 3
0,4 => 000, 100 => 0,1 0,0 0,0 => 10000 = 16
0,5 => 000, 101 => 0,1 0,0 0,1 => 10001 = 17
1,4 => 001, 100 => 0,1 0,0 1,0 => 10010 = 18
1,5 => 001, 101 => 0,1 0,0 1,1 => 10011 = 19
"""

def dec2bin(n, v):
    lst = []
    for i in range(1,n+1):
        digit = 2**(n-i)
        lst.append(v//digit)
        v = v%digit
    return lst

def main():
    n, x, y = map(int, sys.stdin.readline().split())

    x = dec2bin(n,x)
    y = dec2bin(n,y)
    ans = 0
    for i in range(0,2*n,2):
        ans += x.pop() * 2**(i+1) + y.pop() * 2**i
    
    print(ans)

if __name__ == "__main__":
    main()
