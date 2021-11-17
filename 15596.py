# https://www.acmicpc.net/problem/15596
import sys

def solve(a: list) :
    ans = 0
    for i in a : ans += i
    return ans

def main() :
    a = list(map(int, input().split()))
    solve(a)

if __name__=="__main__" :
    main()