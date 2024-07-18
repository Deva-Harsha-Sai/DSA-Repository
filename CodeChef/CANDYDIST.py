for _ in range(int(input())):
    candies,friends = map(int,input().split())
    num = candies/friends
    if num%2==0:
        print("Yes")
    else:
        print("No")