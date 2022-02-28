import sys

# ## BFS
# from collections import deque
# def main():
#     x, y = map(int, sys.stdin.readline().split())

#     cnt = 0
#     queue = deque([y])
#     visit = {y}

#     while x not in visit:
#         temp = deque()
#         for _ in range(len(queue)):
#             y = queue.popleft()
#             if y%2 == 0:
#                 i = y//2
#                 if i not in visit:
#                     visit.add(i)
#                     temp.append(i)
#             for i in {y+1, y-1}:
#                 if i not in visit:
#                     visit.add(i)
#                     temp.append(i)
#         queue = temp
#         cnt += 1

#     print(cnt)


## DP
def hashable(func):
    hash = {}
    def wrapper(*args):
        if args[1] not in hash:
            hash[args[1]] = func(*args)
        return hash[args[1]]
    return wrapper


@hashable
def find_min(x, y):
    if x >= y:
        return x-y
    elif y==1:
        return 1
    elif y%2:
        return 1 + min(find_min(x, y-1),find_min(x, y+1))
    else:
        return min(y-x, 1 + find_min(x,y//2))

def main():
    x, y = map(int,sys.stdin.readline().split())
    print(find_min(x, y))


if __name__ == "__main__":
    main()