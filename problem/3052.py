# https://www.acmicpc.net/problem/3052
import sys

def main() :
    rlist = []
    for _ in range(10) :
        rlist.append(int(sys.stdin.readline())%42)
    print(len(set(rlist))) ## 세트로 중복 제거

if __name__=="__main__" :
    main()