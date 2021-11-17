# https://www.acmicpc.net/problem/1085
import sys

def main() : ##
    x,y,w,h = map(int, sys.stdin.readline().split())
    print(min(w-x, x, h-y, y))

if __name__=="__main__" :
    main()
