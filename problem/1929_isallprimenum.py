# https://www.acmicpc.net/problem/1929
import sys

def isprimenum(n) : ## Check Prime Num.
    for i in range(2,int(n**0.5)+1):
        remind = n%i
        if remind == 0 :
            return False
    if n <= 1 : False
    return True

## Sieve of Eratosthenes 에라토스테네스의 체
def isallprimenum(n) : ## n보다 작은 모든 소수 체크.
    primenum_check = [True]*(n+1) ## 각 숫자가 prime num인지 확인, 아니면 False로 바꿈 ex) 숫자 10은 num_check[10] = False
                             ## 각 인덱스에 숫자를 직접 동기화 하기 위해 n+1까지 만듦.
    primenum_check[0] = False ## 0은 소수가 아님.
    primenum_check[1] = False ## 1은 소수가 아님.

    ## 2보다 크고 입력 n+1 보다 작은 모든 prime N 체크.
    for i in range(2, int((n+1)**0.5)): ## (n+1)^0.5 보다 작은 수의 배수들만 확인하면 됨.
        if primenum_check[i]: # i=2부터 시작해서 i가 True로 되어있으면 i의 배수를 전부 False로 바꿈
            for j in range(2*i, n+1, i):
                primenum_check[j] = False
                # print(num_check)
    return primenum_check ## 결과를 리스트로 반환. list[n] 원하는 숫자 n을 리스트 인덱스에 넣으면 소수인지 TF로 알려줌.

def main() : ## isprimenum을 사용. 대신 매우 느림... 빠른 방법은 main2
    ### Input
    a, b = map(int, sys.stdin.readline().split())
    
    ### Initial Condition
    fixed_a = a
    if a % 2 == 0 : 
        a += 1
    list_primenum = list(range(a,b+1,2))
    if fixed_a == 1 or fixed_a == 2 : 
        if not b == 1 : list_primenum.append(2)
        if fixed_a == 1 : list_primenum.pop(0)
    
    ### Main Loop
    set_primenum = set()
    for i in list_primenum :
        if isprimenum(i) is True :
            set_primenum.add(i)
    
    ### Answer Loop
    for i in sorted(list(set_primenum)) :
        print(i)

def main2() : ## isprimenum은 하나 씩 확인하는 것이라, 한 번에 확인하는 isallprimenum 사용.
    a, b = map(int, sys.stdin.readline().split())

    num_check = isallprimenum(b)

    for i in range(a, b+1):
        if num_check[i] == True:
            print(i)

if __name__=="__main__" :
    main2()
