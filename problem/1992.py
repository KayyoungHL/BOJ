import sys

def divide(li):
    total = sum(map(sum,li))
    n = len(li)
    if total == n**2:
        return "1"
    elif total == 0:
        return "0"
    else:
        div = n//2
        li1 = [li[i][0:div] for i in range(0,div)]
        li2 = [li[i][div:n] for i in range(0,div)]
        li3 = [li[i][0:div] for i in range(div,n)]
        li4 = [li[i][div:n] for i in range(div,n)]
        return f"({divide(li1)}{divide(li2)}{divide(li3)}{divide(li4)})"


def main():
    n = int(sys.stdin.readline().strip())
    li = [list(map(int,list(sys.stdin.readline().strip()))) for _ in range(n)]
    print(divide(li))


if __name__ == "__main__":
    main()