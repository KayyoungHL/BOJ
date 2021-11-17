# https://www.acmicpc.net/problem/1436
import sys

def main() : 
    n = int(sys.stdin.readline())
    
    set_lst = set()
    for i in range(n) :
        x = str(i).zfill(len(str(n)))
        for j in range(len(str(n))+1):
            y = x[:j]+"666"+x[j:]
            set_lst.add(int(y))
    
    print(sorted(list(set_lst))[n-1])

if __name__=="__main__" :
    main()