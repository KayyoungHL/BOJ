import sys

def main():
    n, target = map(int,sys.stdin.readline().split())
    coins = [int(sys.stdin.readline()) for _ in range(n)]
    ans = 0
    for _ in range(n):
        x = coins.pop()
        if target >= x:
            ans += target//x
            target %= x

    print(ans)


if __name__ == "__main__":
    main()