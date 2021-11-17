# https://www.acmicpc.net/problem/1011
import sys

def main() : pass ## 너무 느려서 더 쉬운 방법을 찾음.
    # n = int(sys.stdin.readline())
    # for _ in range(n) :
    #     a,b = map(int, sys.stdin.readline().split())
    #     distance = b-a

    #     n_warp = 0
    #     possible_move = 1
    #     while True :
    #         n_warp += 1

    #         if n_warp % 2 == 0 :
    #             possible_move = n_warp*(n_warp+2)/4
    #         else :
    #             possible_move += (n_warp+1)/2
    #         if possible_move >= distance : 
    #             # print("워프,이동 :",n_warp, int(possible_move))
    #             print(n_warp)
    #             break

def main2() : ## 자연수 합의 역 찾기 : sqrt + 내림을 활용해서 손쉽게 구할 수 있다. -> n(n+1)/2 의 n 찾기
    n = int(sys.stdin.readline())
    for _ in range(n) :
        a,b = map(int, sys.stdin.readline().split())
        distance = b-a
        sqrt_warp_n = int((distance-1)**0.5) 
        warp_n = 0
        if  distance <= sqrt_warp_n*(sqrt_warp_n+1) :
            warp_n = sqrt_warp_n * 2
        else :
            warp_n = sqrt_warp_n * 2 + 1
        print(warp_n)

if __name__=="__main__" :
    main2()
