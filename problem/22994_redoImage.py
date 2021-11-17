# https://www.acmicpc.net/problem/22994
import sys

def divider (in_value=0,divided=1): # in_value / divided = value * divided + remind
    value = in_value//divided
    remind = in_value%divided
    return value, remind

def divisor (in_value): ## set of divisor
    divisor_set = set()
    for i in range(1,int(in_value**0.5)+1):
        (value, remind) = divider(in_value,i)
        if remind == 0 :
            divisor_set.add(i)
            divisor_set.add(value)
    return divisor_set

def findmultinum (inputdata, dis) :
    for di in sorted(dis) :
        if di not in dis : continue
        if type(inputdata) == str : data_split = set()
        else : data_split = []
        for i in range(0, len(inputdata), di) :
            if type(inputdata)==str : data_split.add(inputdata[i:i+di])
            else : data_split.append(inputdata[i:i+di])
        # print(data_split)
        for i in data_split :
            data_splitlencheck = set()
            for j in range(0, len(i)) :
                data_splitlencheck.add(i[j])
            # print(data_splitlencheck)
            if not len(data_splitlencheck) == 1 :
                # print(f"{di} is not multi!!! BREAK")
                dis.remove(di)
                for j in sorted(dis) : 
                    if j%di == 0 : dis.remove(j)
                break
    dis.add(1)
    
    return sorted(dis)[-1]

def main() : 
    n = list(map(int, sys.stdin.readline().split()))
    y_dis = divisor(n[0])
    x_dis = divisor(n[1])
    y_dis.remove(1)
    x_dis.remove(1)
    y = []
    for i in range(n[0]) :
        y.append(sys.stdin.readline().rstrip())
        xj = findmultinum(inputdata=y[i], dis=x_dis)
    xm = int(n[1]/xj)

    new_y = []
    for i in range(0,n[0]) :
        new_y.append(y[i][::xj])

    yi = findmultinum(inputdata=new_y, dis=y_dis)
    yn = int(n[0]/yi)
    new_y = []
    for i in range(0,n[0],yi) :
        new_y.append(y[i][::xj])
    
    ## ANSWER ##
    print(yn,xm)
    for i in range(yn) :
        print(new_y[i])

if __name__=="__main__" :
    main()

""" TEST DATA
4 8
aaabbccc
aaabbccc 
bbbbaaaa
cccctttt    
   

4 6
aaabbb
aaabbb
cccaaa
cccaaa

3 6
aabbaa
bbaabb
aabbaa

1 1
a
"""