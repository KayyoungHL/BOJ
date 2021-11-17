# https://www.acmicpc.net/problem/8958
import sys

def main() :
    n = int(sys.stdin.readline())
    for _ in range(n) :
        score = 0
        o_score = 1
        a = sys.stdin.readline()
        for i in range(len(a)) :
            if a[i] == "O" : 
                score += o_score
                o_score += 1
            else : o_score = 1
                
        print(score)

if __name__=="__main__" :
    main()