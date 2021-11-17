# https://www.acmicpc.net/problem/2577
import sys

def main() :
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    c = int(sys.stdin.readline())
    
    mul = str(a*b*c)
    for i in range(10) : print(mul.count(f"{i}"))
    
if __name__=="__main__" :
    main()