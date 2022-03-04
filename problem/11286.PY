import sys, heapq

def main():
    n = int(sys.stdin.readline())
    pos_heap = []
    neg_heap = []
    for _ in range(n):
        x = int(sys.stdin.readline())
        if x>0:
            heapq.heappush(pos_heap, x)
        elif x<0:
            heapq.heappush(neg_heap, -x)
        else:
            if pos_heap and neg_heap:
                if pos_heap[0] < neg_heap[0]:
                    print(heapq.heappop(pos_heap))
                else:
                    print(-heapq.heappop(neg_heap))
            elif pos_heap:
                print(heapq.heappop(pos_heap))
            elif neg_heap:
                print(-heapq.heappop(neg_heap))
            else:
                print(0)


if __name__ == "__main__":
    main()