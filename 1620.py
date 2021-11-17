# https://www.acmicpc.net/problem/1620
import sys

def main():
    n, m = map(int,sys.stdin.readline().split())
    count = 1
    p_dic = {}
    for _ in range(n):
        name = sys.stdin.readline().rstrip()
        p_dic[name] = count
        p_dic[str(count)] = name
        count += 1

    for _ in range(m):
        print(p_dic[sys.stdin.readline().rstrip()])

if __name__ == "__main__":
    main()

