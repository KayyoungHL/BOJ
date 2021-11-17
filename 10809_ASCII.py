# https://www.acmicpc.net/problem/10809
import sys

def main() :
    a = sys.stdin.readline().rstrip()
    azlist = [chr(c) for c in range(ord('a'), ord('z')+1)]
    for i in azlist : print(a.find(i),end=" ")

if __name__=="__main__" :
    main()

