# https://www.acmicpc.net/problem/1316
import sys

def main () : 
    n = int(sys.stdin.readline().rstrip())
    group = 0
    for _ in range(n) :
        a = sys.stdin.readline().rstrip()
        str_set = {a[0]}
        for j in range(1,len(a)) :
            pre_str = a[j-1]
            if a[j] in str_set :
                if a[j] == pre_str : continue
                # print("BREAK")
                group -= 1
                break
            else : str_set.add(a[j])
            # print(str_set)
        group += 1
    print(group)

if __name__=="__main__" :
    main()