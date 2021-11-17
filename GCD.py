# from itertools import combinations

def divider (in_value=0,divided=1): pass
    # value = in_value//divided
    # remind = in_value%divided
    # return value, remind

def divisor (in_value): pass
    # divisor_list = []
    # for i in range(1,int(in_value**0.5)+1):
    #     (value, remind) = divider(in_value,i)
    #     if remind == 0 :
    #         # print(i, value)
    #         divisor_list.append(i)
    #         if value not in divisor_list :
    #             divisor_list.append(value)
    #     # print(i)
    # divisor_list.sort()
    # return divisor_list

def commondivisor (*in_values, maximum = False) : pass
    # if type(in_values[0]) is list or type(in_values[0]) is tuple :
    #     in_values = in_values[0]
    # cd_list = []
    # divisor_list = []
    # # print(in_values)
    # for iv in in_values :
    #     if len(divisor_list) == 0 :
    #         for i in range(1,int(iv**0.5)+1) :
    #             (value, remind) = divider(iv,i)
    #             if remind == 0 :
    #                 # print(i, value)
    #                 divisor_list.append(i)
    #                 if value not in divisor_list :
    #                     divisor_list.append(value)
    #             # print(i)
    #         divisor_list.sort()
    #     else :
    #         for i in divisor_list :
    #             (value, remind) = divider(iv,i)
    #             if remind == 0 and i not in cd_list :
    #                 cd_list.append(i)
    # cd_list.sort()
    # # print(cd_list)
    # if len(cd_list) == 0 : 
    #     if maximum is True :
    #         return max(divisor_list)
    #     return divisor_list
    # else :
    #     if maximum is True :
    #         return max(cd_list)
    #     return cd_list

def gcd (*in_values, co=None) : pass
    # total = 0
    # if type(in_values[0]) is list or type(in_values[0]) is tuple :
    #     in_values = in_values[0]

    # if co is None :
    #     for i in range(2,len(in_values)+1) :
    #         comb = list(combinations(in_values,i))
    #         for j in comb :
    #             # j = list(j)
    #             total += commondivisor(j,maximum=True)
    #             # print("Sub total :", commondivisor(j,maximum=True))
    # else :
    #     comb = list(combinations(in_values,co))
    #     for j in comb :
    #         # j = list(j)
    #         total += commondivisor(j,maximum=True)
    #         # print("Sub total :", commondivisor(j,maximum=True))        
    # # print(total)
    # return total

### 유클리드 호제법... 대단한 녀석이군...
def gcd_eucl (x,y) :
    while y:
        x,y = y,x%y
    return x

def main() :
    length=int(input())
    total = 0
    for i in range(length) :
        a = list(map(int, input().split()))
        for i in range(1,len(a)) :
            for j in a[i+1:] :
                total += gcd_eucl(a[i],j)
    print(total)

def main2() : pass
    # (value,remind) = divider(10,3)
    # print(value,remind)
    # divisor_list = commondivisor(1000,maximum = True)
    # print("1000의 최대 약수 :",divisor_list)
    # # print(sum(divisor_list))
    # print("375와 500의 최대 공약수 :",commondivisor(375,500,maximum = True))
    # a=input().split()
    # b=input().split()
    # c=input().split()
    # a = list(map(int, a))
    # b = list(map(int, b))
    # c = list(map(int, c))
    # print(gcd(a,co=2))
    # print(gcd(b,co=2))
    # print(gcd(c,co=2))

if __name__=="__main__" :
    main()