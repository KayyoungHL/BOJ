# https://www.acmicpc.net/problem/2630
import sys


def cut4(n, x):
    n_half = n//2
    x1 = [x[i][0:n_half]   for i in range(0,n_half)]
    x2 = [x[i][0:n_half]   for i in range(n_half,n)]
    x3 = [x[i][n_half:n] for i in range(0,n_half)]
    x4 = [x[i][n_half:n] for i in range(n_half,n)]
    x_cut = [x1, x2, x3, x4]
    blue = white = 0
    for i in range(4):
        k = sum([sum(x_cut[i][j]) for j in range(n_half)])
        if k == 0: white += 1
        elif k == n_half**2: blue += 1
        else: 
            a, b = cut4(n_half,x_cut[i])
            blue += a
            white += b
    return blue, white

def main() :
    n = int(sys.stdin.readline())
    x = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
    
    k = sum([sum(x[j]) for j in range(n)])
    white = blue = 0
    if k == 0: white = 1
    elif k == n**2: blue = 1
    else: blue, white = cut4(n, x)
    print(white)
    print(blue)

if __name__=="__main__" :
    main()