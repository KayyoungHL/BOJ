# https://www.acmicpc.net/problem/2920
import sys


def main() :
    n = list(map(int,sys.stdin.readline().split()))
    chka = []
    chkd = []
    for i in range(7) :
        chka.append(n[i] < n[i+1])
        chkd.append(n[i] > n[i+1])

    if sum(chka) == 7 : print("ascending")
    elif sum(chkd) == 7 : print("descending")
    else : print("mixed")

if __name__=="__main__" :
    main()