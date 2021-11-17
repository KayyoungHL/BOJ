# https://www.acmicpc.net/problem/10950
def main() :
    a = int(input())
    total = 0
    for i in range(1,a+1) :
        total += i
    print(total)

def main2() :
    n = int(input())
    print(int(n*(n+1)/2))

if __name__=="__main__" :
    main2()