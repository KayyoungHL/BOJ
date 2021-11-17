# https://www.acmicpc.net/problem/18870
import sys

def main() :
    n = int(sys.stdin.readline())

    lst = list(map(int,sys.stdin.readline().split()))
    
    counts_dict = {}
    for i,x in enumerate(lst) :
        counts_dict[x] = counts_dict.get(x,[]) + [i] ## 사전에 값과 인덱스 순서쌍을 저장
    
    sorted_counts_by_keys = sorted(counts_dict.items()) ## 값을 낮은 순서대로 정렬

    for i in range(len(counts_dict)) :
        for j in sorted_counts_by_keys[i][1] :
            lst[j] = i ## 리스트에 인덱스에 대응하는 0부터 시작하는 값 저장

    for i in range(n) : ## 불러오기
        print(lst[i],end=" ")

def main2() : ## 이런 아이디어가 필요하다. 훨씬 빠르고 메모리도 적게 사용함.
    input=sys.stdin.readline

    n=int(input())
    lst=list(map(int,input().split()))

    set_list=sorted(list(set(lst))) ## 세트를 활용해서 중복 제거 하고 낮은 순 정렬. 
    dic ={set_list[i]:i for i in range(len(set_list))} ## 사전에 낮은 순서대로 0, 1, 2 순으로 대응시켜 순서쌍 저장하기

    for i in lst:
        print(dic[i],end=" ") ## 사전에서 lst에 대응하는 순서쌍 불러오기

if __name__=="__main__" :
    main()