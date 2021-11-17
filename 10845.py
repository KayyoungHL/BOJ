# https://www.acmicpc.net/problem/10845
import sys

def main():
    n = int(sys.stdin.readline())

    queue = []
    start = 0
    for _ in range(n):
        m = len(queue[start:])
        inp = sys.stdin.readline().split()
        if inp[0] == "push":
            queue.append(inp[1])
        elif inp[0] == "pop": 
            if m==0: print(-1)
            else: 
                print(queue[start])
                start +=1
        elif inp[0] == "size": print(m)
        elif inp[0] == "empty":
            if m==0: print(1)
            else: print(0)
        elif inp[0] == "front":
            if m==0: print(-1)
            else: print(queue[start])
        elif inp[0] == "back":
            if m==0: print(-1)
            else: print(queue[-1])            
        

if __name__ == "__main__":
    main()