def max_distance(arr,l):
    max=distance=0
    
    for i in range(l):
        for j in range(l-1,i,-1):
            if arr[i]== arr[j]:
                distance = j-i+1
                break
        if max <distance:
             max= distance
    return max-1


# 2nd approch using hashing make it optimal
def maximum_distance(arr,l):
    maxdistance = 0
    hashing = {}
    for i in range(l):
        if arr[i] not in hashing.keys():
            hashing[arr[i]]=i
        else:
            maxdistance = max(maxdistance,i-hashing[arr[i]])
    return maxdistance

arr = [1,4,2,6,8,4,1,4,2,3,1 ,5,4 ,7 ,8]
x= (max_distance(arr,len(arr)))
if x<=0:
    print("no elements found to match")
else:
    print(x)
x= (maximum_distance(arr,len(arr)))
if x<=0:
    print("no elements found to match")
else:
    print(x)

