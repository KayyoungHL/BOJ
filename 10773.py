# https://www.acmicpc.net/problem/10773
import sys


def main():
    n = int(sys.stdin.readline())
    lists = []
    total = 0
    for _ in range(n):
        x = int(sys.stdin.readline())
        if x == 0 : total -= lists.pop()
        else: 
            lists.append(x)
            total += x
    print(total)

if __name__ == "__main__":
    main()