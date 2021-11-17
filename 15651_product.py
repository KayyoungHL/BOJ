# https://www.acmicpc.net/problem/15651
import sys
from itertools import product

def func(m, n_list, m_str) :
    if m > 0 :
        for i in n_list :
            func(m-1,n_list,(m_str+" "+i))
    else : sys.stdout.write(m_str[1:]+"\n")

def main() :
    n, m = map(int,sys.stdin.readline().split())
    n_list = list(map(str, range(1, n+1)))
    m_str = ""
    func(m,n_list,m_str)

def main2() : ## itertools.product 함수를 사용해서도 가능하다.
    n, m = map(int,sys.stdin.readline().split())
    n_list = list(map(str,range(1, n+1)))
    for p in map(" ".join, product(n_list, repeat=m)) : sys.stdout.write(p+"\n")

if __name__=="__main__" :
    main()