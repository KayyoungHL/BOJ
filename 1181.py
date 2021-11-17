# https://www.acmicpc.net/problem/1181
import sys

def main() :
    n = int(sys.stdin.readline())
    lst = set()
    for _ in range(n) :
        lst.add(sys.stdin.readline().rstrip())

    lst = sorted(sorted(list(lst)),key=len)
    for i in lst :
        sys.stdout.write(str(i)+"\n")

if __name__=="__main__" :
    main()