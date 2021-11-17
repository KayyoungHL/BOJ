# https://www.acmicpc.net/problem/10952
def main() :
    while True :
        a = list(map(int, input().split()))
        if a[0] +  a[1] == 0 :
            break
        print(a[0]+a[1])

if __name__=="__main__" :
    main()