import sys


# 피보나치 수열이 되는구만
# def hashable(func):
#     hash = {}
#     def wrapper(*args):
#         if args not in hash:
#             hash[args] = func(*args)
#         return hash[args]
#     return wrapper

# @hashable
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n*factorial(n-1)

# def main():
#     n = int(sys.stdin.readline())
    
#     sums = 0
#     for i in range((n)//2+1):
#         sums += int((factorial(n-i)/factorial(n-i*2)/factorial(i))%10007)

#     print(sums)

def main():
    n = int(sys.stdin.readline())

    a, b = 0, 1
    for _ in range(1,n+1):
        a, b = b, (a+b)%10007

    print(b)


if __name__ == "__main__":
    main()