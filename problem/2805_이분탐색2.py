# https://www.acmicpc.net/problem/2805
import sys
from collections import Counter

def main():
    k, n = map(int,sys.stdin.readline().split())
    lists = Counter(map(int,sys.stdin.readline().split())).items() # tuple list of (나무의 높이, 높이가 같은 나무의 개수)

    start = 1
    end = max(lists)[0]
    
    while start<=end:
        mid = (start + end)//2
        comp = sum([(height-mid)*num if height-mid>0 else 0 for height, num in lists])
        # print(start, mid, end, comp)
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