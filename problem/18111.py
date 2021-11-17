# https://www.acmicpc.net/problem/18111
import sys

def check (gro, mean, b) : 
    time = 0
    for i in range(len(gro)) :
        if gro[i] > mean :
            time += (gro[i] - mean) * 2
            b += gro[i] - mean
        elif gro[i] < mean :
            time += (mean - gro[i]) * 1
            b -= mean - gro[i]
        gro[i] = mean
    return time, mean

def main() :
    n, m, b = map(int,sys.stdin.readline().split())
    gro = []
    for _ in range(n) :
        gro += list(map(int,sys.stdin.readline().split()))
    gro.sort()
    
    mean = gro[int(2*n*m/3)]
    if mean*m*n > sum(gro)+b : 
        mean = int((sum(gro)+b)/(n*m))

    x,y = check (gro.copy(), mean, b)
    
    print(x,y)
    # for i in range(50,150) : print(check (gro.copy(), i, b))


if __name__=="__main__" :
    main()


"""
4 4 300
30 30 30 30
30 30 30 33
30 30 33 33
30 30 33 33

3 6 500
100 100 100 0 0 0
0 0 0 0 0 70
205 205 205 200 200 85

3 3 30
1 2 3
4 5 6
7 8 9

2 4 10
1 2 3 4 
5 6 7 8 
"""