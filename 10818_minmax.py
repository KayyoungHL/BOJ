# https://www.acmicpc.net/problem/10818
import sys

def main() : ## 450ms. Is it better??
    n = input()
    a = list(map(int, sys.stdin.readline().split()))
    print(min(a),max(a))

def main2() : ## 500ms
    n = int(input())
    a = list(map(int, sys.stdin.readline().split()))
    min = a[0]
    max = a[0]
    for i in a[1:] :
        if min > i : min = i
        if max < i : max = i
    print(min,max)

if __name__=="__main__" :
    main()
    # main2()