# https://www.acmicpc.net/problem/1003
def fibonacci (n) :
    if n == 0 :
        a = 1
        b = 0
        return a,b
    elif n == 1 :
        a = 0
        b = 1
        return a,b
    else :
        a = 1
        b = 1
        c = 0
        for _ in range(2,n) :
            c = a
            a = b
            b += c
        return a,b

def main() :
    case = int(input())
    for _ in range(case) :
        n = int(input())
        num_0, num_1 = fibonacci(n)
        print(num_0,num_1)

if __name__=="__main__" :
    main()

# 1 1 2 3 5 8 13 21 34
# 1 2 3 4 5 6 7  8  9

