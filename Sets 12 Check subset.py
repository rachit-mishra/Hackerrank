for i in range(int(input())):
    a = int(input()); A = set(input().split())
    b = int(input()); B = set(input().split())

    temp = A.issubset(B)
    print(temp)