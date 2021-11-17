# https://www.acmicpc.net/problem/9613
def gcd_eucl (x,y) :
    while y:
        x,y = y,x%y
    return x

def main ():
    length=int(input())
    for i in range(length) :
        total = 0
        a = list(map(int, input().split()))
        for i in range(1,len(a)) :
            for j in a[i+1:] :
                total += gcd_eucl(a[i],j)
        print(total)

if __name__=="__main__" :
    main()