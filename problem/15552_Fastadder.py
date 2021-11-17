# https://www.acmicpc.net/problem/15552
import sys

def main() :
    n = int(input())
    for _ in range(n) :
        print(sum(list(map(int, sys.stdin.readline().split()))))

if __name__=="__main__" :
    main()