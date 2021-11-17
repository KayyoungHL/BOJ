# https://www.acmicpc.net/problem/2581
import sys
### 1929.py는 n보다 작은 모든 자연수의 소수 확인

def isprimenum(n) : ## 소수 확인할 때 쓰는 함수.
    for i in range(2,int(n**0.5)+1):
        remind = n%i
        if remind == 0 :
            return False
    if n == 1 : False
    return True    

def main() : ## 낭비되는 메모리를 조금 줄일 수 있다.
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
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
    if len(set_primenum) == 0 : print(-1)
    else : 
        print(sum(set_primenum))
        print(min(set_primenum))

def main2() : pass  ## 미리 set 그룹을 만들어야 해서 메모리를 조금 쓴다. 어째선지 속도는 조금 빠름.
    # a = int(sys.stdin.readline())
    # b = int(sys.stdin.readline())
    
    # fixed_a = a
    # if a % 2 == 0 : 
    #     a += 1
    # list_primenum = list(range(a,b+1,2))
    # if fixed_a == 1 or fixed_a == 2 : 
    #     if not b == 1 : list_primenum.append(2)
    #     if fixed_a == 1 : list_primenum.pop(0)
    # set_primenum = set(list_primenum)
    # for i in list_primenum :
    #     for j in range(2,int(i**0.5)+1):
    #         remind = i%j
    #         if remind == 0 :
    #             set_primenum.remove(i)
    #             break
    # if len(set_primenum) == 0 : print(-1)
    # else : 
    #     print(sum(set_primenum))
    #     print(min(set_primenum))
    # print("lst : ",sorted(list(set_primenum)))

if __name__=="__main__" :
    main()
