# https://www.acmicpc.net/problem/1463
import sys

def hashable(func):
    hash = {}
    def wrapper(*args):
        if args not in hash:
            hash[args] = func(*args)
        return hash[args]
    return wrapper


@hashable
def find_min(x):
    if x == 1 : return 0
    if x < 4 : return 1
    if   x%6 == 0:
        return 1 + min(find_min(x//2),find_min(x//3))#,find_min(x-1)
    elif x%3 == 0:
        return 1 + min(find_min(x//3),find_min((x-1)//2)+1)
    elif x%2 == 0:
        if (x-1)%3==0:
            return 1 + min(find_min(x//2),find_min((x-1)//3)+1)
        elif (x-2)%3==0:
            return 1 + min(find_min(x//2),find_min((x-2)//3)+2)
    else:
        return 1 + find_min(x-1)
    

def main():
    n = int(sys.stdin.readline())
    print(find_min(n))


if __name__ == "__main__":
    main()

