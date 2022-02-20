from collections import deque
import sys
input = sys.stdin.readline


def main():
    n_ladder, n_snake = map(int,input().split())
    info = {int(k):int(v) for k, v in (input().split() for _ in range(n_ladder+n_snake))}
    table = [0]*101
    depth = 1

    deq = deque(range(2,8))
    temp = set()
    while table[100] == 0:
        cur = deq.popleft()
        while cur in info:
            cur = info[cur]
        if table[cur] == 0:
            table[cur] = depth
            for i in range(1,7):
                if cur+i < 100:
                    temp.add(cur+i)
                elif cur+i == 100:
                    return print(depth+1)
        if len(deq) == 0:
            deq = deque(temp)
            temp = set()
            depth += 1


if __name__ == "__main__":
    main()