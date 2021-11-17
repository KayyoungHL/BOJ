# https://www.acmicpc.net/problem/14889
import sys
import itertools

def main() : # 첫 풀이
    n = int(sys.stdin.readline())
    n_list = list(range(n))
    p_list = []
    for _ in n_list :
        p_list.append((list(map(int,sys.stdin.readline().split()))))
    
    for i in n_list[:-1] :
        for j in n_list[i+1:] :
            p_list[i][j] += p_list[j][i]
            p_list[j][i] = 0
    
    team = list(itertools.combinations(n_list,int(n/2)))
    n_team = int(len(team)/2)

    p_diff = None
    for i in range(n_team) :
        p_a = 0
        p_b = 0
        a_team = team[i]
        for j in range(len(a_team)-1) :
            for k in range(j+1,len(a_team)) :
                p_a += p_list[a_team[j]][a_team[k]]
        b_team = team[-i-1]
        for j in range(len(b_team)-1) :
            for k in range(j+1,len(b_team)) :
                p_b += p_list[b_team[j]][b_team[k]]
        if not p_diff == None : 
            if p_diff > abs(p_a-p_b) : p_diff = abs(p_a-p_b)
        elif p_diff == 0 : break
        else : p_diff = abs(p_a-p_b)
    print(p_diff)

def main1() : # 아래 고수의 풀이를 보고 수정한 풀이
    n = int(sys.stdin.readline())
    n_list = list(range(n))
    p_list = []
    for _ in n_list :
        p_list.append((list(map(int,sys.stdin.readline().split()))))

    sum_h = []    # 가로합
    sum_v = [0]*n    # 세로합
    for i in n_list :
        sum_h.append(sum(p_list[i]))
        for j in n_list :
            sum_v[i] += p_list[j][i]
    
    team = list(itertools.combinations(n_list,int(n/2)))
    n_team = int(len(team)/2)

    p_diff = None
    for i in range(n_team) :
        p_a = 0
        p_b = 0

        for j in team[i] : p_a += sum_h[j]
        for j in team[-1-i] : p_b += sum_v[j]

        if not p_diff == None : 
            if p_diff > abs(p_a-p_b) : p_diff = abs(p_a-p_b)
        elif p_diff == 0 : break
        else : p_diff = abs(p_a-p_b)
    print(p_diff)

def main2 () : ## 와... 천재다 ㄹㅇ...  걍 다 더하고 빼주면 공통된 부분을 제거해서 공통적이지 않은 부분의 차이를 구할 수 있다.
    N = int(sys.stdin.readline()) // 2
    M = 2*N
    stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
    allstat = sum(newstat) // 2

    mins = 65535

    for l in itertools.combinations(newstat[:-1], N):
        mins = min(mins, abs(allstat - sum(l)))
    print(mins)


if __name__=="__main__" :
    main1()