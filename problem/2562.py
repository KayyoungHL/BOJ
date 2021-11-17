# https://www.acmicpc.net/problem/2562
import sys

def main() :
    maximun = int(sys.stdin.readline())
    idx = 1
    max_idx = 1
    while True :
        idx += 1
        if idx == 10 :
            break        
        a = int(sys.stdin.readline())
        if maximun < a : 
            maximun = a
            max_idx = idx
        
    print(maximun)
    print(max_idx)

if __name__=="__main__" :
    main()