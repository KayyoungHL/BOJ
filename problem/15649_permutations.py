# https://www.acmicpc.net/problem/15649
import sys
from itertools import permutations

def func(m, n_list, m_list) :
    for idx, i in enumerate(n_list) :
        remain_n = n_list.copy()
        remain_n.pop(idx)
        m_list.append(i)
        if len(m_list) == m : sys.stdout.write(" ".join(map(str,m_list))+"\n")
        else : func(m,remain_n,m_list)
        m_list.pop()

def main() :
    n, m = map(int,sys.stdin.readline().split())
    n_list = list(map(str, range(1, n+1)))
    m_list = []
    func(m,n_list,m_list)

def main2() : ## itertools.permutations 함수를 사용해서도 가능하다.
    n, m = map(int,sys.stdin.readline().split())
    n_list = list(map(str, range(1, n+1)))
    for p in map(" ".join, permutations(n_list, m)) : sys.stdout.write(p+"\n")

if __name__=="__main__" :
    main()