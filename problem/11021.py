# https://www.acmicpc.net/problem/11021
import sys

def main() :
    n = int(input())
    for i in range(1,n+1) :
        print(f"Case #{i}: {sum(list(map(int, sys.stdin.readline().split())))}")

if __name__=="__main__" :
    main()