# https://www.acmicpc.net/problem/22993
import sys

def main() : 
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    na = a[0]
    while True :
        a = sorted(a)
        idx = a.index(na)
        if len(a) == 1 :
            print("Yes")
            break
        if idx == 0 :
            print("No")
            break
        a[idx] = sum(a[:idx+1])
        del a[:idx]
        na = a[0]
        # print(a)


if __name__=="__main__" :
    main()