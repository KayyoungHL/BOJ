
import sys
from collections import deque

def bfs(table, n, m):
    table[0][0] = "0"
    queue = deque(((0,0),))
    length = 1
    cnt = 1
    
    def check(x):
        i,j = x
        if 0 <= i < n and 0 <= j < m:
            if table[i][j]=="1":
                table[i][j] = "0"
                return True
        return False
        
    while length != 0:
        for _ in range(length):
            i, j = queue.popleft()
            if i == n-1 and j == m-1:
                return cnt
            next = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            queue.extend((x for x in next if check(x)))
        cnt += 1
        length = len(queue)


def main():
    n, m = map(int,sys.stdin.readline().split())
    table = [list(sys.stdin.readline().strip()) for _ in range(n)]
    print(bfs(table, n, m))


if __name__ == "__main__":
    main()