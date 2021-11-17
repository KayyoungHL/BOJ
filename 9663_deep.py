# https://www.acmicpc.net/problem/9663
import sys

# def func(n, imp_pos = [], count = 0, deep = 0) :
    # # if n == 1 : return 1 # n = 1일 때 예외처리
    # possible = set(range(n))#\
    #     # -set(imp_pos)\
    #     # -set(map(lambda x : x - (len(imp_pos) - imp_pos.index(x)),imp_pos))\
    #     # -set(map(lambda x : x + (len(imp_pos) - imp_pos.index(x)),imp_pos))
    
    # for idx, i in enumerate(imp_pos) :
    #     possible -= set((i-(deep-idx),i,i+(deep-idx)))

    # for i in possible :
    #     # print((deep,i))
    #     imp_pos.append(i)
    #     if deep+1 == n : 
    #         del imp_pos[-2:]
    #         return count + 1, imp_pos
    #     count, imp_pos = func(n, imp_pos, count, deep + 1)
    
    # if deep == 0 : return count ## 0행에서 발생하는 에러 예외처리
    # else : 
    #     del imp_pos[-1]
    #     return count, imp_pos

# def func2(n) : # 글로벌 변수로 처리한 함수
    # global imp_pos, count, deep

    # possible = set(range(n))
    # for idx, i in imp_pos :
    #     x = deep-idx
    #     possible -= set((i-x,i,i+x))

    # for i in possible :
    #     if not deep == n-1 :
    #         imp_pos.append((deep,i))
    #         deep += 1
    #         func2(n)
    #         deep -= 1
    #     else : count += 1
        
    # if deep == 0 : return ## 0행에서 발생하는 에러 예외처리
    # else : del imp_pos[-1]

def func3(n, possible, possible_lr, possible_rl, count = 0, deep = 0) :
    for i in range(n) :
        if possible[i] == True & possible_lr[i+deep] == True & possible_rl[(i-deep)+n-1] == True : 
            if deep == n-1 : return count + 1
            possible[i] = possible_lr[i+deep] = possible_rl[(i-deep)+n-1] = False
            count = func3(n, possible,possible_lr,possible_rl, count, deep + 1)
            possible[i] = possible_lr[i+deep] = possible_rl[(i-deep)+n-1] = True
    return count

def main() :
    n = int(sys.stdin.readline())
    # if n == 1 : print(1) ## n=1일 때 예외처리
    # # elif n == 14 : print(365596) ### 타임에러 문제 해결을 위해 14 말고는 다 통과하는 지 확인을 위한 임시 정답 입력
    # else : 
    possible = [True] * n
    possible_lr = [True] * (2*n-1)
    possible_rl = [True] * (2*n-1)
    print(func3(n,possible,possible_lr,possible_rl))

if __name__=="__main__" :
    # imp_pos = []
    # count = 0
    # deep = 0
    main()