# https://www.acmicpc.net/problem/10869
def main() :
    a = list(map(int, input().split()))
    print(a[0]+a[1])
    print(a[0]-a[1])
    print(a[0]*a[1])
    print(a[0]//a[1])
    print(a[0]%a[1])

if __name__=="__main__" :
    main()