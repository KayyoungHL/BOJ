# https://www.acmicpc.net/problem/11022
import sys

def main() :
    n = int(input())
    for i in range(1,n+1) :
        a,b=map(int, sys.stdin.readline().split())
        print(f"Case #{i}: {a} + {b} = {a+b}")

if __name__=="__main__" :
    main()