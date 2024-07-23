for _ in range(int(input())):
    n = int(input())
    ls = []
    for i in range(1,n+1):
        if i%2==0:
            ls.insert(0,str(i))
        else:
            ls.append(str(i))
    print(' '.join(ls))
    