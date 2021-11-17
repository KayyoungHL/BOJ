# https://www.acmicpc.net/problem/1193
import sys

def main2 () : pass  # 테이블 생성 함수. 모든 항목을 인쇄할 때 사용 가능..하지만 요소를 바로 보기엔 부적합!
    # a = int(sys.stdin.readline().rstrip())
    # roop = 0
    # i = 1
    # j = 1
    # count = 1
    # if not count == a :
    #     while True :
    #         roop += 1
    #         if i > j :
    #             i += 1
    #             count += 1
    #             for _ in range(roop) :
    #                 if count == a : break
    #                 j +=1
    #                 i -=1
    #                 count += 1
    #             if count == a : break
    #         else :
    #             j += 1
    #             count += 1
    #             for _ in range(roop) :
    #                 if count == a : break
    #                 j -=1
    #                 i +=1
    #                 count += 1
    #             if count == a : break

    # print(f"{i}/{j}")

def main() : ## 적절한 해법
    a = int(sys.stdin.readline().rstrip()) -1

    line_diagonal = 1 # 대각선 줄 숫자. 1은 첫번째 대각선을 의미(1개 짜리)
    i = int()
    j = int()
    if a == 0 : print("1/1")
    else : 
        while True :
            line_diagonal += 1
            a -= line_diagonal
            if a <= 0 : break
        sumij = line_diagonal + 1
        if line_diagonal % 2 == 0 : ## 짝수 라인 대각선일 때
            j = 1 - a 
            i = sumij - j
        else : ## 홀수 라인 대각선일 때
            i = 1 - a 
            j = sumij - i
        print(f"{i}/{j}")

if __name__=="__main__" :
    main()