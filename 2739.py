# https://www.acmicpc.net/problem/2739
def main() :
    a = int(input())
    for i in range(1,10) :
        print(f"{a} * {i} = {a*i}")
        
if __name__=="__main__" :
    main()