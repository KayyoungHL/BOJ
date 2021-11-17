# https://www.acmicpc.net/problem/1966
import sys


def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        queue = list(map(lambda x:(int(x),"oth"), sys.stdin.readline().split()))
        queue[y] = (queue[y][0],"ans")
        start = 0
        ans = 0
        ma = max(queue)[0]
        while True:
            while queue[start][0]!=ma:
                queue.append(queue[start])
                start +=1
            start +=1
            ans += 1
            if queue[start-1][1] == "ans":
                print(ans)
                break
            ma = max(queue[start:])[0]


if __name__ == "__main__":
    main()