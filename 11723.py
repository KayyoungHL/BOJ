# https://www.acmicpc.net/problem/11723
import sys

def main():
    n = int(sys.stdin.readline())
    sets = [0]*21
    for _ in range(n):
        inp = sys.stdin.readline().split()
        if   inp[0] == "add"   : sets[int(inp[1])] = 1
        elif inp[0] == "remove": sets[int(inp[1])] = 0
        elif inp[0] == "check" : print(sets[int(inp[1])])
        elif inp[0] == "toggle": sets[int(inp[1])] = 0 if sets[int(inp[1])]==1 else 1
        elif inp[0] == "all"   : sets = [1]*21
        elif inp[0] == "empty" : sets = [0]*21

if __name__ == "__main__":
    main()