# https://www.acmicpc.net/problem/1546
import sys

def main() :
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    m = max(a)
    print(sum(a)*100/n/m)

if __name__=="__main__" :
    main()