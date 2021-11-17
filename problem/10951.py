# https://www.acmicpc.net/problem/10951
def main() :
    while True :
        try :
            a = list(map(int, input().split()))
            print(a[0]+a[1])
        except :
            break

if __name__=="__main__" :
    main()