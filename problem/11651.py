# https://www.acmicpc.net/problem/11651
import sys

def main() :
    n = int(sys.stdin.readline())
    lst = []
    for _ in range(n) :
        lst.append(list(map(int,sys.stdin.readline().split())))

    lst = sorted(lst,key=lambda x : (x[1],x[0]))
    for i in lst :
        sys.stdout.write(str(i[0])+" "+str(i[1])+"\n")

if __name__=="__main__" :
    main()