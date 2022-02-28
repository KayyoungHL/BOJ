import sys
import heapq
from collections import defaultdict, deque

def dfs(table, visit, v, ans):
    heap = table[v][:]
    for _ in range(len(heap)):
        x = heapq.heappop(heap)
        if x in visit:
            visit.remove(x)
            ans.append(str(x))
            dfs(table, visit, x, ans)


def bfs(table, v, ans):
    queue = deque((v,))
    while len(queue)!=0:
        heap = queue.popleft()
        for _ in range(len(heap)):
            x = heapq.heappop(heap)
            if x in table:
                ans.append(str(x))
                queue.append(table.pop(x))


def main():
    _, m, v = map(int,sys.stdin.readline().split())
    table = defaultdict(list)
    for _ in range(m):
        i, j = map(int,sys.stdin.readline().split())
        heapq.heappush(table[i], j)
        heapq.heappush(table[j], i)        

    if v in table:
        visit = set(table)
        visit.remove(v)
        ans = [str(v)]
        dfs(table, visit, v, ans)
        print(*ans)

        ans = [str(v)]
        bfs(table, table.pop(v), ans)
        print(*ans)
    else:
        print(v)
        print(v)

if __name__ == "__main__":
    main()