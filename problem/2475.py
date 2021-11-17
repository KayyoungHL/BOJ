# https://www.acmicpc.net/problem/2475
import sys


def main() :
    a, b, c, d, e = list(map(int,sys.stdin.readline().split()))
    
    print((a**2+b**2+c**2+d**2+e**2)%10)


if __name__=="__main__" :
    main()