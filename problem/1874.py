# https://www.acmicpc.net/problem/1874
import sys


def main():
    n = int(sys.stdin.readline())
    stack = []
    num = 1
    ans = ""
    for _ in range(n):
        x = int(sys.stdin.readline())
        while stack[-1:]!=[x]:
            stack.append(num)
            ans += "+\n"
            num += 1
            if stack[-1]>x : return print("NO")
        stack.pop()
        ans += "-\n"
    print(ans)

if __name__ == "__main__":
    main()