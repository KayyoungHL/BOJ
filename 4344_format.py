# https://www.acmicpc.net/problem/4344
import sys

def main() :
    n = int(sys.stdin.readline())
    for _ in range(n) :
        a = list(map(int, sys.stdin.readline().split()))
        a_sum = sum(a[1:])
        mean = a_sum/a[0]
        count = 0
        for i in range(1, a[0]+1) :
            if a[i] > mean :
                count +=1
        print(f"{count/a[0]*100:.3f}%")

if __name__=="__main__" :
    main()