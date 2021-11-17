# https://www.acmicpc.net/problem/10828
import sys

def main():
    n = int(sys.stdin.readline())

    stack = []
    for _ in range(n):
        m = len(stack)
        inp = sys.stdin.readline().split()
        if inp[0] == "push":
            stack.append(inp[1])
        elif inp[0] == "pop": 
            if m==0: print(-1)
            else: print(stack.pop())
        elif inp[0] == "size": print(m)
        elif inp[0] == "empty":
            if m==0: print(1)
            else: print(0)
        elif inp[0] == "top":
            if m==0: print(-1)
            else: print(stack[-1])
        

if __name__ == "__main__":
    main()