# https://www.acmicpc.net/problem/2750
import sys

def main() : 
    n = int(sys.stdin.readline())
    
    set_lst = set()
    for _ in range(n) :
        set_lst.add(int(sys.stdin.readline()))
    x = sorted(list(set_lst))
    for i in range(n) :
        sys.stdout.write(str(x[i])+"\n")
        

if __name__=="__main__" :
    main()