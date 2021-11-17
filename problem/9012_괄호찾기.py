# https://www.acmicpc.net/problem/9012
import sys

def check(x):
    stack = [x[0]]
    for i in x[1:] :
        if i == "(": stack.append(i)
        elif len(stack)!=0:
            if (stack[-1] == "("): stack.pop()
            else : return print("NO")
        else: return print("NO")
    if len(stack) == 0: return print("YES")
    else: return print("NO")


def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        x = sys.stdin.readline().rstrip()
        check(x)


if __name__ == "__main__":
    main()

"""6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()("""