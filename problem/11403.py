import sys

def floydwarshall(n, dp):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][j]=="1" or (dp[i][k]=="1" and dp[k][j]=="1"):
                    dp[i][j] = "1"
    return dp

def main():
    n = int(sys.stdin.readline())
    admatr = [sys.stdin.readline().split() for _ in range(n)]

    floydwarshall(n, admatr)
    for i in admatr:
        print(" ".join(i))

if __name__ == "__main__":
    main()