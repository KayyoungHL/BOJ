import sys

## 틀렸는데 이유를 모르겠다... 이유 알아냈다.. 최소값을 잘못 지정함...
# from collections import defaultdict
# def main():
#     n, m = map(int,sys.stdin.readline().split())

#     adlist = {i:defaultdict(set) for i in range(1,n+1)}
#     for _ in range(m):
#         i, j = map(int,sys.stdin.readline().split())
#         adlist[i][0]|=set((i,j))
#         adlist[i][1].add(j)
#         adlist[j][0]|=set((i,j))
#         adlist[j][1].add(i)

#     for dist in range(1,n-1):
#         for i in range(1,n+1):
#             if len(adlist[i][0]) != n:
#                 for j in adlist[i][dist]:
#                     adlist[i][dist+1] |= (adlist[j][1] - adlist[i][0])
#                     adlist[i][0] |= adlist[i][dist+1]
#                     for k in adlist[i][dist+1]:
#                         adlist[k][dist+1].add(i)
#                         adlist[k][0].add(i)
#                     if len(adlist[i][0]) == n:
#                         break

#     min = n*n
#     ans = n+1
#     for i, v in adlist.items():
#         print(i, v)
#         tot = 0
#         for node in v:
#             if node:
#                 tot += node*len(v[node])
#         if tot < min:
#             min = tot
#             ans = i
#         elif tot == min and i < ans:
#             ans = i

#     print(ans)

from collections import deque
def bfs(table, start):
    ans = 0
    visit = [True]*len(table)
    visit[start] = False
    queue = deque((start,))
    n = len(queue)
    cnt = 1

    def check(x):
        if visit[x]:
            visit[x] = False
            return True
        else:
            return False

    while n != 0:
        ans += cnt*n
        for _ in range(n):
            x = queue.popleft()
            queue.extend((i for i in table[x] if check(i)))
        cnt += 1
        n = len(queue)
    return ans


def main():
    n, m = map(int,sys.stdin.readline().split())
    adlist = {i:set() for i in range(n)}
    for _ in range(m):
        i, j = map(int,sys.stdin.readline().split())
        adlist[i-1].add(j-1)
        adlist[j-1].add(i-1)

    min = n*n
    ans = n
    for i in adlist:
        tot = bfs(adlist, i)
        if tot < min:
            min = tot
            ans = i
        elif tot == min and i < ans:
            ans = i
    print(ans+1)
        

if __name__ == "__main__":
    main()