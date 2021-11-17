# https://www.acmicpc.net/problem/2675
import sys

def main () : 
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n) :
        a = sys.stdin.readline().split()
        k = int(a[0])
        s = a[1]
        for j in s : print(j*k,end="")
        print()

if __name__=="__main__" :
    main()