# https://www.acmicpc.net/problem/9095
import sys

def cacheable(func):
    cache = {}
    def wrapper(n):
        if not n in cache.keys():    
            cache[n] = func(n)
        return cache[n]
    return wrapper


@cacheable
def factorial(n):
    if n == 0 : return 1
    if n <= 2: return n
    return n*factorial(n-1)


def func(n):
    count = 0
    for i in range((n)//3+1):
        m = n-i*3
        for j in range((m)//2+1):
            l = m-j*2
            count += factorial((i+j+l))/factorial(i)/factorial(j)/factorial(l)
    return int(count)


def main(): 
    n = int(sys.stdin.readline())
    for _ in range(n):
        print(func(int(sys.stdin.readline())))


def main2():
    n = int(sys.stdin.readline())
    arr = [1, 2, 4]
    for i in range(4,11):
        arr.append(sum(arr[-3:]))
    for _ in range(n):
        print(arr[int(sys.stdin.readline())-1])

        
if __name__=="__main__" :
    main2()
