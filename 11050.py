# https://www.acmicpc.net/problem/11050
import sys

def combination(higher,lower) :
        if lower == 0 :
            return 1
        answer = higher/lower
        for i in range(1,lower) :
            answer = answer*(higher-i)/(lower-i)
        return round(answer)


def main():
    n, k = map(int,sys.stdin.readline().split())
    print(combination(n,k))


if __name__ == "__main__":
    main()
    