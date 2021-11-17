# https://www.acmicpc.net/problem/14888
import sys
import itertools

# def back_tracking (n, n_list, operator, o_min=None, o_max=None, out = 0) : ## 시간초과 난다.
    # c_out = out
    # for _ in range(1,n) :
    #     for ope in ["+","-","*","/"] :
    #         if not operator[ope] == 0 :
    #             operator[ope] -= 1
    #             if ope == "+" : out += n_list[0]
    #             elif ope == "-" : out -= n_list[0]
    #             elif ope == "*" : out = out * n_list[0]
    #             else : out = int(out / n_list[0])
    #             # print(n,out,o_max,o_min)
    #             if not n-1 == 1 : o_max, o_min = back_tracking(n-1, n_list[1:], operator, o_min=o_min, o_max=o_max, out=out)
    #             else :
    #                 if not o_min == None :
    #                     if out > o_max : o_max = out
    #                     if out < o_min : o_min = out
    #                 else :
    #                     o_min = out 
    #                     o_max = out
    #             out = c_out
    #             operator[ope] += 1
    # return o_max, o_min

def main() :
    n = int(sys.stdin.readline())
    n_list = (list(map(int,sys.stdin.readline().split())))
    a,s,p,d = map(int,sys.stdin.readline().split())
    # operator = {"+":a,"-":s,"*":p,"/":d}
    # for i in back_tracking(n, n_list[1:], operator, out=n_list[0]) :
    #     print(i)

    operator = ["+"]*a + ["-"]*s + ["*"]*p + ["/"]*d
    # print(len(list(itertools.permutations(operator))))
    # print(len(set(itertools.permutations(operator))))
    # print(set(itertools.permutations(operator)))
    o_min = None
    o_max = None
    out = None
    for i in set(itertools.permutations(operator)) :
        out = n_list[0]
        for idx, j in enumerate(i) :
            if j == "+" : out += n_list[idx+1]
            elif j == "-" : out -= n_list[idx+1]
            elif j == "*" : out = out * n_list[idx+1]
            else : out = int(out / n_list[idx+1])
        if not o_min == None :
            if out > o_max : o_max = out
            if out < o_min : o_min = out
        else :
            o_min = out 
            o_max = out
    print(o_max)
    print(o_min)

if __name__=="__main__" :
    main()