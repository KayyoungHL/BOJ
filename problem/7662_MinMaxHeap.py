import sys
import heapq

### 최소힙에서 최대값을 찾아서 제거하는건 O(n)의 시간이 들어서 시간초과가 발생한다.
# def delete(heap, n) -> None:
#     if len(heap) == 0:
#         return
#     if n == "1":
#         # max heap
#         max = [None, 0]
#         for i, v in enumerate(heap):
#             if max[0]:
#                 if v > max[0]:
#                     max[0] = v
#                     max[1] = i
#             else:
#                 max[0] = v
#                 max[1] = i
#         if max[1] == len(heap)-1:
#             heap.pop()
#         else:
#             heap[max[1]], heap[-1] = heap[-1], heap[max[1]]
#             heap.pop()
#             heapq._siftup(heap, max[1])
#     else:
#         # min heap
#         heapq.heappop(heap)

# def main():
#     n = int(sys.stdin.readline())
#     heap = []
#     for _ in range(n):
#         m = int(sys.stdin.readline())
#         for _ in range(m):
#             com, num = sys.stdin.readline().split()
#             if com == "I":
#                 heapq.heappush(heap, int(num))
#             else:
#                 delete(heap, num)
#         if len(heap) == 0:
#             print("EMPTY")
#         else:
#             max = [None, 0]
#             for i, v in enumerate(heap):
#                 if max[0]:
#                     if v > max[0]:
#                         max[0] = v
#                         max[1] = i
#                 else:
#                     max[0] = v
#                     max[1] = i

#             print(heap[max[1]], heap[0])

### 최소힙과 최대힙을 같이 쓰는 풀이
def main():
    n = int(sys.stdin.readline())

    for _ in range(n):
        heap_n = []
        heap_p = []
        visit = {}
        m = int(sys.stdin.readline())
        for _ in range(m):
            com, num = sys.stdin.readline().split()
            if com == "I":
                heapq.heappush(heap_n, int(num))
                heapq.heappush(heap_p, -int(num))
                visit[int(num)] = visit.get(int(num),0) + 1
            else:
                if len(visit) != 0:
                    if num == "1":
                        x = -heapq.heappop(heap_p)
                        while x not in visit:
                            x = -heapq.heappop(heap_p)
                        visit[x] -= 1
                        if visit[x] == 0:
                            del visit[x]
                    else:
                        x = heapq.heappop(heap_n)
                        while x not in visit:
                            x = heapq.heappop(heap_n)
                        visit[x] -= 1
                        if visit[x] == 0:
                            del visit[x]
        
        if len(visit):
            while -heap_p[0] not in visit:
                heapq.heappop(heap_p)
            while heap_n[0] not in visit:
                heapq.heappop(heap_n)
            print(-heap_p[0], heap_n[0])
        else:
            print("EMPTY")


if __name__ == "__main__":
    main()