# https://www.acmicpc.net/problem/15829
import sys

def main():
    n = int(sys.stdin.readline())
    h = list(map(lambda x:ord(x)-96,list(sys.stdin.readline().strip())))

    ans = 0
    for i in range(n):
        temp = 1
        for _ in range(i):
            temp = temp%1234567891 * 31
        ans += h[i]*temp
    print(ans%1234567891)

if __name__ == "__main__":
    main()
