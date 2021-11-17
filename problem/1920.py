# https://www.acmicpc.net/problem/1920
import sys

def main() :
    n = int(sys.stdin.readline())
    a = set((map(int,sys.stdin.readline().split())))
    m = int(sys.stdin.readline())
    b = list(map(int,sys.stdin.readline().split()))
        
    for i in b :
        if i in a : print(1)
        else : print(0)

if __name__=="__main__" :
    main()