# https://www.acmicpc.net/problem/2162
import sys
from collections import Counter

def crosscheck (cor1, cor2) :
    a, b, c, d = cor1[0]
    w, x, y, z = cor2[0]
    c, d, w, x, y, z = c-a, d-b, w-a, x-b, y-a, z-b
    # print((a-a,b-b),(c,d),(w,x),(y,z))
    l = (c**2+d**2)**0.5
    
    c1 = (c*c+d*d)/l

    w1 = (c*w+d*x)/l
    x1 = (-d*w+c*x)/l

    y1 = (c*y+d*z)/l
    z1 = (-d*y+c*z)/l

    if x1*z1 <= 0 :
        if ((w1 < 0) & (y1 < 0)) | ((w1 > c1) & (y1 > c1)) : cross = False
        elif w1 == y1 : cross = True
        elif x1 == z1 == 0 : cross = True
        else :
            if 0 <= w1-(y1-w1)/(z1-x1)*x1 <= c1 : cross = True
            else : cross = False
    else : cross = False
    if cross : return (cor1[1], cor2[1])
    else : return False

def main() :
    n = int(sys.stdin.readline())
    cord_set = []
    for i in range(n) :
        cord_set.append((list(map(int,sys.stdin.readline().split())),i))
    
    cross_num = []
    for i in range(n-1):
        for j in range(i+1,n):
            k = crosscheck(cord_set[i],cord_set[j])
            if k : cross_num.append(k)
    
    print(cross_num)
    # 여기서 부터 탐색 문제!!
    # 2667, 11279 참조할 것!
    
if __name__=="__main__" :
    main()


    """

13
0 0 1 1
1 1 2 2
3 3 4 4
4 4 5 5
5 5 6 6
6 6 7 7
8 8 9 9
9 9 10 10
10 10 11 11
11 11 12 12
12 12 13 13
2 2 3 3
5 5 12 12



    """