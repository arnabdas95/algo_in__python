def find(arr,n,k):
    occurence = 0
    for i in range(n):
        arr[i]=str(arr[i])

    arr=''.join(arr)
    for i in arr:
        if i==str(k):
            occurence +=1
    return occurence



if __name__ == '__main__':
    arr = [11,12,13,14,15]
    x = find(arr,len(arr),1)
    print(x)


