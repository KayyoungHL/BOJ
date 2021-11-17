# https://www.acmicpc.net/problem/20149
import sys

def main() :
    a, b, c, d = map(int,sys.stdin.readline().split())
    w, x, y, z = map(int,sys.stdin.readline().split())

    c, d, w, x, y, z = c-a, d-b, w-a, x-b, y-a, z-b
    # print((a-a,b-b),(c,d),(w,x),(y,z))
    l = (c**2+d**2)**0.5
    
    a1 = 0
    b1 = 0

    c1 = (c*c+d*d)/l
    d1 = (-d*c+c*d)/l

    w1 = (c*w+d*x)/l
    x1 = (-d*w+c*x)/l

    y1 = (c*y+d*z)/l
    z1 = (-d*y+c*z)/l

    # print((a1,b1),(c1,d1),(w1,x1),(y1,z1))
    n, m = None, None
    chk = False
    if x1*z1 <= 0 :
        if ((w1 < 0) & (y1 < 0)) | ((w1 > c1) & (y1 > c1)) : print(0)
        elif w1 == y1 : # 교점의 좌표 (w1, 0)
            print(1)
            n, m = w1, 0
        elif x1 == z1 == 0 : 
            print(1) # 교점의 좌표 (? ,0) 
            one = ((w1 == 0) & (y1 < 0))
            two = ((w1 < 0) & (y1 == 0))
            thr = ((w1 == c1) & (y1 > c1))
            fou = ((w1 > c1) & (y1 == c1))
            # print(one, two, thr, fou)
            if   one+two == 1 : n, m = 0, 0
            elif thr+fou == 1 : n, m = c1, 0
        else :
            chk = w1-(y1-w1)/(z1-x1)*x1 
            if 0 <= chk <= c1 : 
                print(1) # 교점의 좌표 = (chk, 0)
                n, m = (chk, 0)
            else : print(0)
    else : print(0)
    # print((n,m))
    if not (n, m) == (None, None) :
        n1 = (c*n-d*m)/l + a
        m1 = (d*n+c*m)/l + b
        print(n1, m1)

if __name__=="__main__" :
    main()