# https://www.acmicpc.net/problem/2775
import sys

def combination(higher,lower) :
        if lower == 0 :
            return 1
        answer = higher/lower
        for i in range(1,lower) :
            answer = answer*(higher-i)/(lower-i)
        return round(answer)

def main() :
    a = int(sys.stdin.readline())
    for _ in range(a) :
        k = int(sys.stdin.readline()) + 1
        n = int(sys.stdin.readline()) - 1
        higher = n+k
        lower = None
        
        if n>k : 
            lower = k
        else : 
            lower = n
        print(combination(higher,lower))
        
if __name__=="__main__" :
    main()
