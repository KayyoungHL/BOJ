# https://www.acmicpc.net/problem/1065
import sys

def checkhannumber(n) :
    diff_list = []
    if len(str(n)) > 1 :
        for i in range(len(str(n))-1) :
            diff_list.append(int(str(n)[i])-int(str(n)[i+1]))
        if len(set(diff_list)) == 1 : return 1
        else : return 0
    else : return 1

def main() : 
    a = int(sys.stdin.readline())
    count = 0
    for i in range(1,a+1) :
        if checkhannumber(i) == 1 :
            count += 1
    print(count)

if __name__=="__main__" :
    main()