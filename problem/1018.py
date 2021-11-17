# https://www.acmicpc.net/problem/1018
import sys

def main() : 
    y,x = map(int, sys.stdin.readline().split())
    
    ans1 = ['WBWBWBWB', 'BWBWBWBW']


    board = []
    for _ in range(y) :
        board.append(sys.stdin.readline().rstrip())
    # print(board)

    lcount = [[] for _ in range(y)]
    for j in range(y) :
        if j%2 == 0 : ans = ans1[0]
        else : ans = ans1[1]
        for i in range(x-7) :
            if board[j][i:i+8] == ans :
                lcount[j].append(0)
            else :
                count = 0
                for k in range(8) :
                    if board[j][i+k] == ans[k] : continue
                    else : count += 1
                lcount[j].append(count)
    # print(lcount)
    y_count = list(zip(*lcount))
    # print(y_count)
    lstsum = []
    for i in range(x-7) :
        for j in range(y-7) :
            subsum = sum(y_count[i][j:j+8])
            if subsum > 32 :
                subsum = 64 - subsum
            lstsum.append(subsum)
    # print(lstsum)
    print(min(lstsum))

if __name__=="__main__" :
    main()