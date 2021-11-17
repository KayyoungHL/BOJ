# https://www.acmicpc.net/problem/9020
import sys

## Sieve of Eratosthenes 에라토스테네스의 체
def isallprimenum(n) : ## n보다 작은 모든 소수 체크.
    primenum_check = [True]*(n+1) ## 각 숫자가 prime num인지 확인, 아니면 False로 바꿈 ex) 숫자 10은 primenum_check[10] = False
                             ## 각 인덱스에 숫자를 직접 동기화 하기 위해 n+1까지 만듦.
    primenum_check[0] = False ## 0은 소수가 아님.
    primenum_check[1] = False ## 1은 소수가 아님.

    ## 2보다 크고 입력 n+1 보다 작은 모든 prime N 체크.
    for i in range(2, int((n+1)**0.5)+1): ## (n+1)^0.5 보다 작은 수의 배수들만 확인하면 됨.
        if primenum_check[i] == True: # i=2부터 시작해서 i가 True로 되어있으면 i의 배수를 전부 False로 바꿈
            for j in range(2*i, n+1, i):
                primenum_check[j] = False
                # print(primenum_check)
    return primenum_check

def main() : ##
    primenum_check = isallprimenum(10000)
    n = int(sys.stdin.readline())
    for _ in range(n) :
        a = int(sys.stdin.readline())
        for i in range(int(a/2)) :
            x2 = int(a/2)+i
            x1 = a-x2
            if primenum_check[x2] == True and primenum_check[x1] == True :
                print(x1,x2)
                break

if __name__=="__main__" :
    main()
