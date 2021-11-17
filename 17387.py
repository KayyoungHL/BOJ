# https://www.acmicpc.net/problem/17387
import sys

def main() :
    a, b, c, d = map(int,sys.stdin.readline().split())
    w, x, y, z = map(int,sys.stdin.readline().split())

    a, b, c, d, w, x, y, z = 0, 0, c-a, d-b, w-a, x-b, y-a, z-b
    # print((a,b),(c,d),(w,x),(y,z))
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

    if x1*z1 <= 0 :
        if ((w1 < 0) & (y1 < 0)) | ((w1 > c1) & (y1 > c1)) : print(0)
        elif w1 == y1 : print(1)
        elif x1 == z1 == 0 : print(1)
        else :
            chk = w1-(y1-w1)/(z1-x1)*x1
            if 0 <= chk <= c1 : print(1)
            else : print(0)
    else : print(0)

if __name__=="__main__" :
    main()