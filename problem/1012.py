import sys
from collections import deque

def bfs(table):
    unvisit = set(table)
    cnt = 0
    for key in table:
        if key not in unvisit:
            continue
        queue = deque((key,))
        unvisit.remove(key)
        temp = deque()
        while len(queue) != 0:
            x = queue.pop()
            for y in table[x]:
                if y in unvisit:
                    unvisit.remove(y)
                    temp.append(y)
            queue = temp
        cnt += 1
        if len(unvisit) == 0:
            break
    return cnt


def main():
    n = int(sys.stdin.readline())

    for _ in range(n):
        _,_,z = map(int, sys.stdin.readline().split())
        table = {tuple(int(i) for i in sys.stdin.readline().split()):set() for _ in range(z)}
        for i,j in table:
            if (i+1,j) in table:
                table[(i,j)].add((i+1,j))
            if (i-1,j) in table:
                table[(i,j)].add((i-1,j))
            if (i,j+1) in table:
                table[(i,j)].add((i,j+1))
            if (i,j-1) in table:
                table[(i,j)].add((i,j-1))
        print(bfs(table))


if __name__ == "__main__":
    main()

