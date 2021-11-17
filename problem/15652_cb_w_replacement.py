# https://www.acmicpc.net/problem/15652
import sys
from itertools import combinations_with_replacement

def func(m, n_list, m_str) :
    remain_n = n_list.copy()
    for i in n_list :
        if m <= 1 : sys.stdout.write((m_str+" "+i).lstrip()+"\n")
        else : func(m-1,remain_n,m_str+" "+i)
        remain_n.pop(0)

def main() :
    n, m = map(int,sys.stdin.readline().split())
    n_list = list(map(str, range(1, n+1)))
    m_str = ""
    func(m,n_list,m_str)

def main2() : ## 
    n, m = map(int,sys.stdin.readline().split())
    n_list = list(map(str, range(1, n+1)))
    for p in map(" ".join, combinations_with_replacement(n_list, m)) : sys.stdout.write(p+"\n")

if __name__=="__main__" :
    main2()