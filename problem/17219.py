# https://www.acmicpc.net/problem/17219
import sys

def main():
    n, m = map(int,sys.stdin.readline().split())

    p_dic = {}
    ans = []
    for _ in range(n):
        key, value = sys.stdin.readline().split()
        p_dic[key] = value

    for _ in range(m):
        x = sys.stdin.readline().rstrip()
        print(p_dic[x])

if __name__ == "__main__":
    main()

