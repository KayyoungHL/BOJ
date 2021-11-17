# https://www.acmicpc.net/problem/2579
import sys

#### 동적 계획법 배우고 재도전한다...
def hashable(func):
    hash = {}
    def wrapper(steps, xlist):
        if len(xlist)>100 : return func(steps, xlist)
        if xlist not in hash:
            hash[xlist] = func(steps, xlist)
        return hash[xlist]
    return wrapper

@hashable
def summ(steps, xlist):
    if len(xlist) < 1:return 0
    return summ(steps, xlist[:-1]) + steps[xlist[-1]]

def stepdown(x, xlist,steps):
    if not x-3<0:
        xlist.append(x-3)
        a = stepdown(x-3,xlist,steps)
        xlist.pop()
    else: return summ(steps, tuple(xlist))
    if not x-2<0:
        xlist.append(x-2)
        b = stepdown(x-2,xlist,steps)
        xlist.pop()
    return min(a, b)

def main():
    n = int(sys.stdin.readline())
    steps = [int(sys.stdin.readline()) for _ in range(n)]
    print(sum(steps)-stepdown(n,[],steps))

if __name__ == "__main__":
    main()

