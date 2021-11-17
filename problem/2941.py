# https://www.acmicpc.net/problem/2941
import sys

def main () : 
    n = sys.stdin.readline().rstrip()

    a = ["c=", "c-", "d-", "lj", "nj", "s=", "dz=", "z="]
    for i in a :
        n = n.replace(i,"_")
        # print(n)
    print(len(n))

if __name__=="__main__" :
    main()