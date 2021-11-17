# https://www.acmicpc.net/problem/4948
import sys


def isallprimenum(n) : ## n보다 작은 모든 소수 체크.
    
    num_check = [True]*(n+1) ## 각 숫자가 prime num인지 확인, 아니면 False로 바꿈 ex) 숫자 10은 num_check[10] = False
                             ## 각 인덱스에 숫자를 직접 동기화 하기 위해 n+1까지 만듦.
    num_check[0] = False ## 0은 소수가 아님.
    num_check[1] = False ## 1은 소수가 아님.

    ## 2보다 크고 입력 n+1 보다 작은 모든 prime N 체크.
    for i in range(2, int((n+1)**0.5)+1): ## (n+1)^0.5 보다 작은 수의 배수들만 확인하면 됨.
        if num_check[i] == True: # i=2부터 시작해서 i가 True로 되어있으면 i의 배수를 전부 False로 바꿈
            for j in range(2*i, n+1, i):
                num_check[j] = False
                # print(num_check)
    return num_check

def main() : ## isprimenum은 하나 씩 확인하는 것이라, 한 번에 확인하는 방법.
    num_check = isallprimenum(123456*2)
    while True :
        n = int(sys.stdin.readline())
        if n == 0 : break        
        print(num_check[n+1:2*n+1].count(True))

if __name__=="__main__" :
    main()
