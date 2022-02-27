# import sys

# sys.setrecursionlimit(10000)
# def dfs(cur, adjlist, unvisit):
#     for i in adjlist[cur]:
#         if unvisit[i-1]:
#             unvisit[i-1] = False
#             dfs(i, adjlist, unvisit)


# # from collections import deque
# # def bfs(adjlist, unvisit):
    
# #     cnt = 0
# #     for i in adjlist:
# #         if unvisit[i-1]:
# #             unvisit[i-1] = False
# #             queue = deque([i])
# #         else:
# #             continue

# #         while len(queue) != 0:
# #             temp = deque()
# #             for _ in range(len(queue)):
# #                 x = queue.popleft()
# #                 for i in adjlist[x]:
# #                     if unvisit[i-1]:
# #                         unvisit[i-1] = False
# #                         temp.append(i)
# #             queue = temp
# #         cnt += 1
# #     return cnt



# def main():
#     n, m = map(int, sys.stdin.readline().split())
    
#     unvisit = [True]*(n)
#     adjlist = {i:set() for i in range(1,n+1)}
#     for _ in range(m):
#         i, j = map(int, sys.stdin.readline().split())
#         adjlist[i].add(j)
#         adjlist[j].add(i)
    
#     cnt = 0
#     while sum(unvisit) != 0:
#         cur = unvisit.index(True)
#         unvisit[cur] = False
#         dfs(cur+1,adjlist,unvisit)
#         cnt += 1
#     print(cnt)

#     # print(bfs(adjlist, unvisit))

# if __name__ == "__main__":
#     main()


import sys

def main():
    nodes = dict()
    nets = dict()

    n, m = map(int, sys.stdin.readline().split())
    for i in range(n):
        nodes[i + 1] = i
        nets[i] = [i + 1]

    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())

        if nodes[a] != nodes[b]:
            low = nodes[a]
            high = nodes[b]
            if low > high:
                low, high = high, low
            
            for i in nets[high]:
                nodes[i] = low
                nets[low].append(i)
            del nets[high]

    print(len(nets))

if __name__ == "__main__":
    main()