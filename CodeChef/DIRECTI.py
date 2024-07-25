for _ in range(int(input())):
    size = int(input())
    routeMap = []
    for i in range(size):
        d = list(map(str,input().split()))
        routeMap.append(d)
    directions = []
    places = []
    for route in routeMap:
        place = route[route.index("on")+1:]
        placeadd = ""
        for i in range(len(place)):
            if i<len(place)-1:
                placeadd+=place[i]+" "
            else:
                placeadd+=place[i]
        places.append(placeadd)
        directions.append(route[0])
    places = places[::-1]
    directions = directions[::-1]
    for i in range(len(directions)):
        if directions[i]=="Left":
            directions[i]="Right"
        else:
            directions[i]="Left"
    directions.pop(-1)
    directions.insert(0,"Begin")
    for i in range(len(directions)):
        print(directions[i]+" on "+places[i])
    print()