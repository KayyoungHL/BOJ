# https://www.acmicpc.net/problem/4153
import sys

def main() : ##
    while True :
        x,y,z = map(int, sys.stdin.readline().split())
        xyz2 = [z**2, x**2, y**2]
        if x == 0 and y==0 and z==0 : break
        if sum(xyz2) == max(xyz2) * 2 : print("right")
        else : print("wrong")

if __name__=="__main__" :
    main()
