# https://www.acmicpc.net/problem/9461
import sys


def main() :
    n = int(sys.stdin.readline())

    pre = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    for i in range(10,101) :
        pre.append(pre[i]+pre[i-4])

    for _ in range(n) :
        print(pre[int(sys.stdin.readline())])



if __name__=="__main__" :
    main()