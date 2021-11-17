# https://www.acmicpc.net/problem/4673
import sys

def selfnum(n) :
    sout = int(n)
    for i in str(n) :
        sout += int(i)
    return sout

def main() : # 88 ms, it is better. set is good to remove list value
    a = set(range(1,10001))
    b = []
    for i in range(1,10001) :
        b.append(selfnum(i))
    a = a-set(b)
    for i in sorted(a) :
        print(i)

def main2() : # 216 ms
    a = list(range(1,10001))
    for i in range(1,10001) :
        try :
            a.remove(selfnum(i))
        except :
            continue
    for i in a :
        print(i)

if __name__=="__main__" :
    main()