import sys
import heapq

def main():
    n = int(sys.stdin.readline())
    heap = []
    for _ in range(n):
        com = int(sys.stdin.readline())
        if com:
            heapq.heappush(heap,com)
        else:
            if len(heap):
                print(heapq.heappop(heap))
            else:
                print(0)

if __name__ == "__main__":
    main()

