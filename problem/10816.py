# https://www.acmicpc.net/problem/10816
import sys
from collections import Counter

def main():
    n = int(sys.stdin.readline())
    x = Counter(list(map(int, sys.stdin.readline().split())))
    m = int(sys.stdin.readline())
    y = list(map(int, sys.stdin.readline().split()))
    for i in y :
        print(x[i],end=" ")
    

if __name__ == "__main__":
    main()