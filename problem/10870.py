# https://www.acmicpc.net/problem/10870
import sys

def fibonacci(n) :
    if n == 1 : return 1
    if n == 0 : return 0
    return fibonacci(n-1) + fibonacci(n-2)
    
def main() : ##
    # sys.setrecursionlimit()
    n = int(sys.stdin.readline())
    print(fibonacci(n))

if __name__=="__main__" :
    main()
