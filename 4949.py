# https://www.acmicpc.net/problem/4949
import sys

def check(x):
    stack = []
    stack = []
    for i in x :
        if i == "(": stack.append(i)
        elif i == ")":
            if len(stack) == 0: return print("no")
            elif (stack[-1] == "("): stack.pop()
            elif (stack[-1] == "["): return print("no")
        if i == "[": stack.append(i)
        elif i == "]":
            if len(stack) == 0: return print("no")
            elif (stack[-1] == "["): stack.pop()
            elif (stack[-1] == "("): return print("no")
        
    if len(stack) == 0: return print("yes")
    else: return print("no")


def main():
    while True:
        x = sys.stdin.readline().rstrip()
        if x == ".": break
        check(x)


if __name__ == "__main__":
    main()