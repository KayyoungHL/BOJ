# https://www.acmicpc.net/problem/9375
import sys
from itertools import combinations

def func(lst):
    """경우의 수 문제. 가능한 모든 경우의 수
    예를들어 모자의 가짓수 a, 옷의 가짓수 b, 바지의 가짓수 c 라면
    a중 하나 + 안 고르기 1 => a+1
    b중 하나 + 안 고르기 1 => b+1
    c중 하나 + 안 고르기 1 => c+1
    위 셋의 모든 경우를 옵한 후
    셋 다 안 고른 경우 제외 => -1
    최종 식 = (a+1)(b+1)(c+1)-1
    """
    temp = 1
    for i in lst:
        temp *= (i+1)
    return temp-1


def main(): 
    n = int(sys.stdin.readline())
    for _ in range(n):
        m = int(sys.stdin.readline())
        clothes = {}
        for _ in range(m):
            name, kind = sys.stdin.readline().split()
            clothes[kind] = clothes.get(kind, 0) + 1
        print(func(list(clothes.values())))


if __name__=="__main__" :
    main()
