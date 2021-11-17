# https://www.acmicpc.net/problem/10250
import sys

def main() :
    case_n = int(sys.stdin.readline())
    for _ in range(case_n) :
        h, w, n  = map(int, sys.stdin.readline().split())
        num = 1+n//h
        flr = n%h
        if flr == 0 : 
            num -= 1
            flr = h
        print(f"{flr}{str(num).zfill(2)}")
        
if __name__=="__main__" :
    main()
