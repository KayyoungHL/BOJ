import sys

def get_gcd(a: int,b: int) -> int:
    while a%b != 0:
        a, b = b, a%b

    return b


def coin_exchange(n, target, coins): 
    # 동전의 최대 공약수를 구하면 배열 크기를 줄일 수 있다.
    gcd = coins[0]
    for i in range(1, n):
        gcd = get_gcd(gcd, coins[i])

    # 최대 공약수를 나누어서 새로운 타겟을 구한다.
    new_target = target//gcd

    # 0부터 타겟까지의 배열을 생성한다.
    targets = [0 for _ in range(new_target + 1)] 
    targets[0] = 1
    
    # 가장 작은 동전 부터 차례로 동전을 뽑는다
    # coins.sort()
    for coin in coins:
        # 동전에 최대 공약수를 나눈다.
        coin //= gcd
        
        # 타겟까지 가능한 금액을 모두 계산한다
        for target in range(1,new_target+1):
            # 해당 동전을 하나 빼고 남은 잔돈까지의 경우의 수 
            # + 이전 동전까지 가진 경우의 수 = 새로운 경우의 수
            changes = target - coin
            if changes >= 0:
                targets[target] += targets[changes]
                
    return targets[new_target]


def main():
    input = sys.stdin.readline
    n, target = map(int, input().split())
    coins = [int(input().strip()) for _ in range(n)]
    print(coin_exchange(n,target,coins))


def main2():
    input = sys.stdin.readline
    n, target = map(int, input().split())
 
    targets = [0 for _ in range(target + 1)] 
    targets[0] = 1
    
    for _ in range(n):
        coin = int(input().strip())
        for i in range(1,target+1):
            changes = i - coin
            if changes >= 0:
                targets[i] += targets[changes]
                
    print(targets[target])


if __name__ == "__main__":
    main()