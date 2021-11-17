# https://www.acmicpc.net/problem/10872
import sys

def factorial(n) :
    if n <= 1 : return 1
    return n*factorial(n-1)

def main() : ##
    # sys.setrecursionlimit()
    n = int(sys.stdin.readline())
    print(factorial(n))

if __name__=="__main__" :
    main()
