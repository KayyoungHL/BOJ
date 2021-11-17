# https://www.acmicpc.net/problem/2869
import sys

def main() :
    a,b,v = map(int, sys.stdin.readline().split())

    n = round((v-b)/(a-b))
    if n < (v-b)/(a-b) : n += 1
    print(n)

if __name__=="__main__" :
    main()
