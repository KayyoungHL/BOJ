# https://www.acmicpc.net/problem/11866
import sys

def main():
    n, k = map(int,sys.stdin.readline().split())
    stack = []
    queue = list(range(1,n+1))
    q_sta = 0
    for _ in range(n):
        for _ in range(k-1):
            queue.append(queue[q_sta])
            q_sta += 1
        stack.append(str(queue[q_sta]))
        q_sta += 1
    print("<"+", ".join(stack)+">")


if __name__ == "__main__":
    main()