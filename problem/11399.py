import sys

def main():
    n = int(sys.stdin.readline())
    people = [int(i) for i in sys.stdin.readline().split()]
    
    people.sort()
    ans = 0
    for i, v in enumerate(people):
        ans += v*(n-i)

    print(ans)

if __name__ == "__main__":
    main()