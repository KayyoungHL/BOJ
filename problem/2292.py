# https://www.acmicpc.net/problem/2292
import sys

def main () : 
    a = int(sys.stdin.readline().rstrip())

    a = a - 1
    shell = 1
    if a > 0 :
        while True :
            a = a - 6*shell
            shell += 1
            if a <= 0 : break
    
    print(shell)
        
if __name__=="__main__" :
    main()