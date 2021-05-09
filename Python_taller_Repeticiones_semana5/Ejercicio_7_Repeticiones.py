while True:
    X, M=map(int, input().split())
    if X==0 and M==0:
        break
    Y=X*M
    print(Y)
    