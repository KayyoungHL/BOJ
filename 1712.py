# https://www.acmicpc.net/problem/1712
import sys

def main () : 
    initial_price, made_price, sell_price = map(int,sys.stdin.readline().split())
    if made_price >= sell_price : print(-1)
    else :
        n = initial_price/(sell_price - made_price)
        if n >= round(n) : n +=1
        print(round(n))
        
if __name__=="__main__" :
    main()