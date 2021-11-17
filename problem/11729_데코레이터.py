# https://www.acmicpc.net/problem/11729
import sys

def towerofhanoi(n, a = 1, b = 2, c = 3) :
    if n == 0 : 
        return
    towerofhanoi(n-1, a = a, b = c, c = b)
    print(f"{a} {c}")
    towerofhanoi(n-1, a = b, b = a, c = c)


def cacheable(func): ### 재귀함수 사용할 때 데코레이터 캐시를 검색해서 확인해보자!! 유용할듯 모든 인자가 hashable? 무슨 말일까
    cache = {}
    def u(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return u

@cacheable
def towerofhanoi2(n, a, b, c) :
    if n == 0 : 
        return ""
    lst = []
    lst.append(towerofhanoi2(n-1, a, c, b))
    lst.append(f"{a} {c}\n")
    lst.append(towerofhanoi2(n-1, b, a, c))

    return "".join(lst)
"""
    a -> c 1시작끝
    a -> b 2시작
    c -> b 2끝
    a -> c 3시작
    b -> a
    b -> c
    a -> c 3끝
    a -> b 4시작

    """
def main() :  
    n = int(sys.stdin.readline())
    sys.stdout.write(str(2**n-1)+"\n") ## 총 이동 횟수 2**n-1
    sys.stdout.write(towerofhanoi2(n,1,2,3))

if __name__=="__main__" :
    main()
