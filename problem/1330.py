# https://www.acmicpc.net/problem/1330
def main() :
    a = list(map(int, input().split()))
    if a[0]==a[1] :
        print("==")
    elif a[0]>a[1] :
        print(">")
    else :
        print("<")

if __name__=="__main__" :
    main()