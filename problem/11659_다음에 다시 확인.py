import sys

# def hashable(func):
#     hash = {}
#     def wrapper(i, j, nums):
#         if (i, j) not in hash:
#             hash[(i, j)] = func(i, j, nums)
#         return hash[(i, j)]
#     return wrapper

# @hashable
# def sum(i, j, nums):
#     if i == j-1:
#         return nums[i]
#     if i == j-2:
#         return sum(i, j-1, nums) + sum(i+1, j, nums)
#     return sum(i, j-1, nums) + sum(i+1, j, nums) - sum(i+1, j-1, nums)

# def main():
#     n, m = map(int,sys.stdin.readline().split())
#     nums = [int(i) for i in sys.stdin.readline().split()]
    
#     # diff = 1
#     hash = {(i,i+1):nums[i] for i in range(n)}

#     # diff = 2
#     for i in range(n-1):
#         hash[(i,i+2)] = hash[(i+1,i+2)] + hash[(i, i+1)]
    
#     # diff = 3 ~ n
#     for diff in range(3,n):
#         for i in range(n+1-diff):
#             hash[(i,i+diff)] = hash[(i+1,i+diff)] + hash[(i, i-1+diff)] - hash[(i+1, i-1+diff)]
            
#     for _ in range(m):
#         i, j = map(int,sys.stdin.readline().split())
#         sys.stdout.write(str(hash[(i-1,j)])+"\n")

def main():
    n, m = map(int,sys.stdin.readline().split())
    nums = [int(i) for i in sys.stdin.readline().split()]

    sums = [0]*(n+1)
    for i in range(1,n+1):
        sums[i] = sums[i-1] + nums[i-1]

    print(sums)

    for _ in range(m):
        i, j = map(int,sys.stdin.readline().split())
        sys.stdout.write(str(sums[j]-sums[i-1])+"\n")


if __name__ == "__main__":
    main()
    # print(sum(0,2,[1,2]))