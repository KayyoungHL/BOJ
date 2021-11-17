# https://www.acmicpc.net/problem/3009
import sys

def main() : ##
    x1,y1 = map(int, sys.stdin.readline().split())
    x2,y2 = map(int, sys.stdin.readline().split())
    x3,y3 = map(int, sys.stdin.readline().split())

    if x1 == x2 : x0 = x3
    elif x1 == x3 : x0 = x2
    else : x0 = x1

    if y1 == y2 : y0 = y3
    elif y1 == y3 : y0 = y2
    else : y0 = y1

    print(x0,y0)

if __name__=="__main__" :
    main()
