# https://www.acmicpc.net/problem/2231
import sys

def selfnum(n) :
    sout = int(n)
    for i in str(n) :
        sout += int(i)
    return sout

def main() : 
    a = int(sys.stdin.readline())
    
    start = a-9*len(str(a)) ## 생성자는 그 분해합과 길이*9보다 적게 차이난다.

    if start <= 0 : start = 0
    for i in range(start,a) :
        if selfnum(i) == a : 
            sys.stdout.write(str(i))
            break
        if i == a - 1 : sys.stdout.write("0")
    
    

if __name__=="__main__" :
    main()