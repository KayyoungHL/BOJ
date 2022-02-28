import sys
from collections import deque

def main():
    x, y = map(int,sys.stdin.readline().split())

    maps = []

    queue = deque()
    for i in range(y):
        maps.append([int(x) for x in sys.stdin.readline().split()])
        for j in range(x):
            if maps[i][j] == 1:
                queue.append((i, j))
                maps[i][j] = -1
    
    ## bfs
    cnt = -1
    while len(queue) != 0:
        temp = deque()
        for _ in range(len(queue)):
            i, j = queue.pop()
            if 0 < i < y-1:
                if maps[i+1][j] != -1:
                    temp.append((i+1,j))
                    maps[i+1][j] = -1
                if maps[i-1][j] != -1:
                    temp.append((i-1,j))
                    maps[i-1][j] = -1
            elif i == 0:
                if maps[i+1][j] != -1:
                    temp.append((i+1,j))
                    maps[i+1][j] = -1
            else:
                if maps[i-1][j] != -1:
                    temp.append((i-1,j))
                    maps[i-1][j] = -1
            
            if 0 < j < x-1:
                if maps[i][j+1] != -1:
                    temp.append((i,j+1))
                    maps[i][j+1] = -1
                if maps[i][j-1] != -1:
                    temp.append((i,j-1))
                    maps[i][j-1] = -1
            elif j == 0:
                if maps[i][j+1] != -1:
                    temp.append((i,j+1))
                    maps[i][j+1] = -1
            else:
                if maps[i][j-1] != -1:
                    temp.append((i,j-1))
                    maps[i][j-1] = -1
        queue = temp
        cnt += 1
    if sum((sum(i) for i in maps)) == -x*y:
        print(cnt)
    else:
        print(-1)

if __name__ == "__main__":
    main()