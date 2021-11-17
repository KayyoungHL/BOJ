# https://www.acmicpc.net/problem/7568
import sys

def main() : 
    n = int(sys.stdin.readline())
    
    lsts = []
    for i in range(n) :
        x,y = map(int,sys.stdin.readline().split())
        lsts.append([x,y])
    
    seq_list = []
    for i in lsts :
        count = 1
        for j in lsts :
            if i[0]<j[0] and i[1]<j[1] : count +=1
        seq_list.append(str(count))

    print(" ".join(seq_list))

if __name__=="__main__" :
    main()

"""
9
55 185
60 170
88 177
66 185
58 183
88 186
60 175
53 175
46 155
"""