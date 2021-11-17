# https://www.acmicpc.net/problem/11720
import sys

def main() :
    n = list(map(int, sys.stdin.readline().split()))
    a = (sys.stdin.readline().rstrip())
    total = 0
    for i in a : total += int(i)
    print(total)

if __name__=="__main__" :
    main()