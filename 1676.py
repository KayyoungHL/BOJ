# https://www.acmicpc.net/problem/1676
import sys

def main():
    n = int(sys.stdin.readline())

    ans = 0
    k = 5
    while k<=n:
        ans += len(range(k,n+1,k))
        k *= 5
    print(ans)

if __name__ == "__main__":
    main()

