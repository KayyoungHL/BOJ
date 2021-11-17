# https://www.acmicpc.net/problem/1427
import sys

def main() : 
    n = sys.stdin.readline().rstrip()

    lst = list()
    for i in n : lst.append(i)

    lst.sort(reverse=True)

    for i in lst : print(i,end="")

if __name__=="__main__" :
    main()