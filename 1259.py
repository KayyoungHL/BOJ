# https://www.acmicpc.net/problem/1259
import sys


def chk(a) :
    n = int(len(a)/2)
    for i in range(n) :
        if not a[i] == a[-i-1] : 
            return print("no")
    return print("yes")

def main() :
    a = str()
    while True :
        a = str(sys.stdin.readline().rstrip())
        if a == "0" : break
        chk(a)

if __name__=="__main__" :
    main()