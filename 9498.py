# https://www.acmicpc.net/problem/9498
def main() :
    a = int(input())
    if a>=90 :
        print("A")
    elif a>=80 :
        print("B")
    elif a>=70 :
        print("C")
    elif a>=60 :
        print("D")
    else :
        print("F")


if __name__=="__main__" :
    main()