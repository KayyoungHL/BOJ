# https://www.acmicpc.net/problem/1764
import sys

def main():
    n, m = map(int,sys.stdin.readline().split())

    p_dic = {}
    ans = []
    for _ in range(n):
        p_dic[sys.stdin.readline().rstrip()] = True

    count = 0
    for _ in range(m):
        x = sys.stdin.readline().rstrip()
        if p_dic.get(x,False): 
            ans.append(x)
            count += 1
    
    ans.sort()
    print(count)
    for i in ans:
        print(i)

if __name__ == "__main__":
    main()

