import numpy as np

def gauss_elimination(input_a,input_y=None, inverse=False) :
    if not input_y is None : x=np.concatenate((input_a,input_y),axis=1).astype(float) ## y 입력이 들어올 때 해를 구해준다.
    else : x = input_a.copy().astype(float)
    n = len(x)
    if inverse == True : ## 역행렬 구할 때
        if not len(x[0]) == n : 
            print("정사각 행렬(n x n)만 역행렬을 구할 수 있습니다.")
            return None
        if np.linalg.det(x) == 0 :
            print("비가역 행렬은 역행렬을 구할 수 없습니다.")
            return None
        I=np.identity(n=n, dtype="float")
        x = np.concatenate((x,I),axis=1)
    check = 0
    for i in range(n-1) : ## 가우스 소거법 사용
        if x[i][i] == 0 : 
            check = 0
            for j in range(i+1,n) :
                if x[j][i] == 0 : continue
                # print("break")
                # print(f"{x[i+1]} / {x[i+1][i]} * {x[i][i+1]}")
                temp = (x[i] - x[j] / x[j][i]) ##
                # print(temp)
                if not temp[i] == 0 : 
                    # print(temp/temp[i])
                    x[i] = temp/temp[i]
                elif np.sum(temp) == 0 :
                    x[i] = temp
                else : x[i] = temp/temp[np.where(temp!=0)][0]
                # print("break, 정상동작의 상징")
                check +=1
                break
            check -= 1
            # print("정상이면 0, 비정상이면 -1",check)
        # print("i 중간 체크",i,n)
        for j in range(i+1,n) :
            # print((i-check,j))
            if x[i][i-check] == 0 : continue
            # print(f"{x[i]} / {x[i][i]} * {x[j][i]}")
            # print(x[i] / x[i][i] * x[j][i])
            temp = (x[j] - x[i] / x[i][i-check] * x[j][i-check])
            # print(temp)
            if not temp[i+1] == 0 : 
                # print(temp/temp[i+1+check])
                x[j] = temp/temp[i+1]
            elif np.sum(temp) == 0 :
                x[j] = temp
            else : 
                # print(np.where(temp!=0))
                # print(temp[np.where(temp!=0)])
                x[j] = temp/temp[np.where(temp!=0)][0]
            # print(x)
    
    if (inverse == True) or (input_y is not None) : ## 역행렬 또는 연립방정식의 해를 구할 때
        for i in range(n-1, -1, -1) :
            if x[i][i] == 0 : 
                print("에러 발생! 해를 구할 수 없음")
                return 
            for j in range(i-1,-1,-1) :
                # print(f"{x[i]} / {x[i][i]} * {x[j][i]}")
                x[j] = (x[j] - x[i] / x[i][i] * x[j][i])
                # print(x)
        x = x[:,n:2*n]

    return x

def main():
    # l = np.array([1,2,3])
    # m = np.array([-1,0,7])
    # n = np.array([4,8,2])
    # l = np.array([1,3,1])
    # m = np.array([1,1,-1])
    # n = np.array([3,11,5])

    # 현재 에러 발생하는 부분 예시 -- 해결함!
    l = np.array([1,2,5])
    m = np.array([1,2,3])
    n = np.array([3,6,1])
    
    x = np.array([l,m,n])
    # print(x.dtype)
    print(gauss_elimination(x))
    
    ## y가 있을 때 해를 구해준다.
    y = np.array([[1],[1],[1]])
    # print(gauss_elimination(x,y))
    # print(np.linalg.inv(x))

    ## y가 있을 때 해를 구해준다.
    P = np.array([[0,2,5,3,8,2,4,5],[0,6,12,1,2,1,2,4],[3,0,2,8,4,7,5,6],[2,2,2,2,2,2,2,2],[0,3,0,0,8,2,3,1],[9,3,2,5,1,1,3,1],[3,2,2,1,1,1,4,1],[7,1,3,2,1,7,9,7]])
    y = np.array([[7],[1],[3],[2],[1],[7],[9],[7]])
    # print(np.concatenate((P,y),axis=1).astype(float))
    print(np.round_(gauss_elimination(P,y),2))
    # print(np.round_(np.linalg.inv(P),2))

if __name__=="__main__" :
    main()
    