import datetime

def 타이머 (콜백함수) :
    def 감싸는함수 (*args, **kwargs) :
        시작 = datetime.datetime.now()
        결과 = 콜백함수(*args, **kwargs)
        끝 = datetime.datetime.now()
        걸린시간 = 끝-시작
        print(f"{콜백함수.__name__} 함수를 실행시키는데 걸린 시간은 {걸린시간} 입니다.")
        return 결과
    return 감싸는함수

def cacheable(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@cacheable
def 재귀함수 (a, b) :
    if (a == 0) & (b==0) : return 0
    if a == 0 : 
        결과 = 재귀함수(a, b-1) + 1
        return 결과
    if b == 0 : 
        결과 = 1 + 재귀함수(a-1, b)
        return 결과
    결과 = 재귀함수(a,b-1)+재귀함수(a-1,b)
    return 결과


@cacheable
def fibonachi(n):
    if n <= 1 : return 1
    return fibonachi(n-1) + fibonachi(n-2)


@타이머
def main() :
    # print(재귀함수 (12,12))
    print(fibonachi(50))

if __name__ == "__main__" :
    main()