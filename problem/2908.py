# https://www.acmicpc.net/problem/2908
import sys

def main () : 
    n = sys.stdin.readline().split()
    a = n[0][::-1]
    b = n[1][::-1]
    if a>b : print(a)
    else : print(b)

if __name__=="__main__" :
    main()