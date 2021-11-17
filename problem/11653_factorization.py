# https://www.acmicpc.net/problem/11653
import sys

def isprimenum_change(n) : ## 소수 확인할 때 쓰는 함수를 약간 바꿈. TF와 더불어 i로 나누어 지면 i를 반환함
    for i in range(2,int(n**0.5)+1):
        remind = n%i
        if remind == 0 :
            return False, i
    if n == 1 : False, 1
    return True, n

def factorization(n) : ## 소인수 분해. 사전으로 {소수:제곱수} 로 반환한다. ex) 12 = 2*2*3 -> {2:2, 3:1}
    dict_factorization = {}
    while True :
        tf, i = isprimenum_change(n)
        if tf is True : 
            dict_factorization[n] = dict_factorization.get(n, 0) + 1
            break
        else : 
            dict_factorization[i] = dict_factorization.get(i, 0) + 1
            n = int(n / i)
    return dict_factorization

def main() :
    a = int(sys.stdin.readline())
    if a == 1 : return
    a_fact = factorization(a)
    # print(a_fact)
    for i in range(len(a_fact.keys())) :
        print((str(list(a_fact.keys())[i])+"\n")*a_fact[list(a_fact.keys())[i]],end="")

if __name__=="__main__" :
    main()
