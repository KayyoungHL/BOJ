# https://www.acmicpc.net/problem/2609
import sys

def gcd_eucl (x,y) :
    while y:
        x,y = y,x%y
    return x


def main() :
    a, b = map(int,sys.stdin.readline().split())
    c = gcd_eucl(a,b)
    print(f"{c}\n{int(a*b/c)}")


if __name__=="__main__" :
    main()