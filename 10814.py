# https://www.acmicpc.net/problem/10814
import sys

def main() :
    n = int(sys.stdin.readline())
    lst = list()
    for _ in range(n) :
        x, y = sys.stdin.readline().rstrip().split()
        x = int(x)
        lst.append((x,y))

    lst = sorted(list(lst), key = lambda x : x[0])
    for i in lst :
        sys.stdout.write(str(i[0])+" "+i[1]+"\n")

if __name__=="__main__" :
    main()