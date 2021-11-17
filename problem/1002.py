# https://www.acmicpc.net/problem/1002
def main() :
    n = int(input())
    for i in range(n) :
        a = list(map(int, input().split()))
        dx2 = (a[0]-a[3])**2
        dy2 = (a[1]-a[4])**2
        d = (dx2+dy2)**0.5
        radd = a[2]+a[5]
        rdiff = abs(a[2]-a[5])
        if d == 0 and a[2] == a[5] :
            print(-1)
        elif rdiff < d < radd :
            print(2)
        elif rdiff == d or radd == d:
            print(1)            
        else :
            print(0)

if __name__=="__main__" :
    main()