# https://www.acmicpc.net/problem/2884
def main() :
    a = list(map(int, input().split()))
    if a[1] < 45 :
        b = a[1]+15
        if a[0] == 0 :
            print(23,b)
        else :
            print(a[0]-1,b)
    else :
        print(a[0],a[1]-45)
        


if __name__=="__main__" :
    main()