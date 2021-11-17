# https://www.acmicpc.net/problem/2798
import sys

def main() :  
    n,m = map(int,sys.stdin.readline().split())
    l_card = list(map(int, sys.stdin.readline().split()))
    l_card.sort()
    
    breakall = False
    max_total = 0
    ### 작은 수 부터 합보다 큰 수 부터 합으로 하면 elif 문 하나를 지울 수 있다. 더 빨라지지만... 귀찮으니 다음에
    for i in range(n-2) :
        for j in range(i+1, n-1) :
            sub_tot = l_card[i] + l_card[j]
            if sub_tot + l_card[j] + 1 > m : break
            for k in range(j+1, n) :
                total = sub_tot + l_card[k]
                if total == m : 
                    max_total = total
                    breakall = True ## 함수를 쓰면 return으로 3개의 루프를 한번에 나갈 수 있다. 아래의 의미없는 if문 2개가 사라져서 빨라진다.
                    break
                elif total > m : break
                elif max_total < total < m : max_total = total
            if breakall == True : break
        if breakall == True : break
    sys.stdout.write(str(max_total))

if __name__=="__main__" :
    main()
