# https://www.acmicpc.net/problem/10871
def main() :
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = ""
    for i in range(a[0]) :
        if b[i] < a[1] :
            c = c + str(b[i]) +" "
    print(c.rstrip())

if __name__=="__main__" :
    main()