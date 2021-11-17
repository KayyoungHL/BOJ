# https://www.acmicpc.net/problem/2164
import sys

def main() :
    n = int(sys.stdin.readline())

    x = 0
    surv = n
    while True :
        if n == 1 : 
            print(surv)
            break
        if n%2 == 1 : 
            surv = surv - 2**x
        
        n = round(n/2+0.1)
        x += 1

# def main() : # 1등의 풀이...
#     n = int(sys.stdin.readline())
#     x = 1
#     while x < n :
#         x *= 2
    
#     print(x if x == n else 2*n-s)

if __name__=="__main__" :
    main()