# https://www.acmicpc.net/problem/1978
import sys

def main() : 
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    for i in a :
        if i == 1 : 
            n -= 1
            continue
        for j in range(2,int(i**0.5)+1):
            remind = i%j
            if remind == 0 : 
                n -= 1
                break
    print(n)

if __name__=="__main__" :
    main()
