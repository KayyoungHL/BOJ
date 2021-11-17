# https://www.acmicpc.net/problem/1654
import sys

def main():
    k, n = map(int,sys.stdin.readline().split())
    lists = [int(sys.stdin.readline()) for _ in range(k)]

    start = 1
    end = max(lists)
    
    while start<=end:
        mid = (start + end)//2
        comp = sum([x//mid for x in lists])
        # print(start, mid, end)
        if comp >= n:
            start = mid + 1
        elif comp < n:
            end = mid - 1
    if comp < n :
        print(mid-1)
    else:
        print(mid)
    

if __name__ == "__main__":
    main()
    
    """
4 10
802
743
457
539

9 10
1
1
1
1
1
1
1
100
1000

5 5
5
5
5
5
5
    """