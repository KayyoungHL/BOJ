# https://www.acmicpc.net/problem/1157
import sys

def main () : 
    n = sys.stdin.readline().rstrip().upper()

    azlist = [chr(c) for c in range(ord('A'), ord('Z')+1)]
    cnt = {}
    temp_cnt = 0
    tot_cnt = 0
    
    for i in azlist : 
        temp_cnt = n.count(i)
        temp_list = []
        if not temp_cnt == 0 : 
            if cnt.get(temp_cnt) is None :
                temp_list.append(i)
                cnt[temp_cnt] = temp_list
            else :
                temp_list = cnt.get(temp_cnt)
                temp_list.append(i)
                cnt[temp_cnt] = temp_list
            tot_cnt += temp_cnt
        n = n.replace(i,"")
        # print(cnt)
        # if temp_cnt > (len(n)+tot_cnt)/2 :
        #     print(i)
        #     break
    # print(cnt)
    max_chr = cnt[sorted(list(cnt.keys()))[-1]]
    if len(max_chr) > 1 : print("?")
    elif len(max_chr) == 1 : print(max_chr[0])

if __name__=="__main__" :
    main()