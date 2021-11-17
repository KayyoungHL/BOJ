# https://www.acmicpc.net/problem/10866
import sys

def main():
    n = int(sys.stdin.readline())
    deque = [0]*10000
    start = 10000
    size = 0
    for _ in range(n):
        inp = sys.stdin.readline().split()
        if inp[0] == "push_front":
            start -= 1
            size += 1
            deque[start] = inp[1]
        elif inp[0] == "push_back":
            size += 1
            deque.append(inp[1])
        elif inp[0] == "pop_front": 
            if size==0: print(-1)
            else: 
                size -= 1
                print(deque[start])
                start +=1
        elif inp[0] == "pop_back":
            if size==0: print(-1)
            else: 
                size -= 1
                print(deque.pop())
        elif inp[0] == "size": print(size)
        elif inp[0] == "empty":
            if size==0: print(1)
            else: print(0)
        elif inp[0] == "front":
            if size==0: print(-1)
            else: print(deque[start])
        elif inp[0] == "back":
            if size==0: print(-1)
            else: print(deque[-1])            
        

if __name__ == "__main__":
    main()