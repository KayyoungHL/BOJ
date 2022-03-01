import sys

def main():
    x = sys.stdin.readline().split("-")
    ans = sum(map(int,x[0].split("+")))
    for i in x[1:]:
        ans -= sum(map(int,i.split("+")))
    print(ans)

if __name__ == "__main__":
    main()