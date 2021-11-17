# https://www.acmicpc.net/problem/10430
def main() :
    a = list(map(int, input().split()))
    
    print((a[0]+a[1])%a[2])
    print((a[0]%a[2]+a[1]%a[2])%a[2])
    print((a[0]*a[1])%a[2])
    print((a[0]%a[2]*a[1]%a[2])%a[2])
    
if __name__=="__main__" :
    main()