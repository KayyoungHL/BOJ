# https://www.acmicpc.net/problem/2606
import sys
from collections import Counter

def main():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    pair = [tuple(map(int,sys.stdin.readline().split())) for _ in range(m)]
    com = [-1]*(n+1)
    for i in range(m):
        x = com[pair[i][0]]
        y = com[pair[i][1]]
        if not (x == -1)|(y == -1):
            for j in range(len(com)):
                if com[j] == y: com[j] = x
        elif not x == -1:
            com[pair[i][1]] = x
        elif not y == -1:
            com[pair[i][0]] = y
        else: 
            com[pair[i][0]] = com[pair[i][1]] = i
    print(Counter(com)[com[1]]-1)
        

if __name__ == "__main__":
    main()

    """
7
13
1 2
3 4
5 6
5 3
7 1
7 6
7 4
5 2
3 1
3 2
5 1
6 3
4 2
    """