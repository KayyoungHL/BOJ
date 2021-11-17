# https://www.acmicpc.net/problem/2839
import sys

def main() :
    a = int(sys.stdin.readline())
    r5 = a % 5
    v5 = a // 5

    if r5 == 0 : print(v5)
    elif r5 == 1 and v5 > 0 : 
        print(v5 + 1)
    elif r5 == 2 and v5 > 1 :
        print(v5 + 2)
    elif r5 == 3 :
        print(v5 + 1)
    elif r5 == 4 and v5 > 0 :
        print(v5 + 2)
    else : print(-1)
     
if __name__=="__main__" :
    main()
