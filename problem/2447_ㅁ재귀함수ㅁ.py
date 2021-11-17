# https://www.acmicpc.net/problem/2447
import sys

def star(n,data,__count=0) : ## 최선을 다해 줄여서 통과는 함. 약 800ms
    x = int(n / 3)
    k = n * 3**__count
    loop_range = []
    for i in range(x) :
        loop_range += list(range(x+i,k-x,n))
    for i in loop_range :
        for j in loop_range :
            if i // x % 3 == 1 and j // x % 3 == 1 : 
                data[i][j] = " "    
    if n == 3 :
        return data
    return star(x,data,__count = __count + 1)

def main() :  
    n = int(sys.stdin.readline())
    data = [["*"] * n for _ in range(n)]
    data = star(n, data)
    for i in range(n) :
        data[i] = "".join(data[i])
    sys.stdout.write("\n".join(data))

def star2(x): ## 지...지니어스... ㅠㅠ 이게 진정한 재귀함수... 80ms
    if x == 1:
        return ['*']
    x = x // 3
    a = star(x)
    topbottom = [i * 3 for i in a]
    middle = [i + ' ' * x + i for i in a]
    return topbottom + middle + topbottom

def main2(): 
    n = int(input())
    mystar = '\n'.join(star2(n))
    print(mystar)


if __name__=="__main__" :
    main()
