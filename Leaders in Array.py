#Find all the leaders in a array.
'''Leader in array is the element which is greater or equal to all the elements of  its right side.
The end elements is always is a leader
The time complexity is  O(n)'''

#define function
def  find_leaders(arr , size):
    # as last elements is always is a leader element so return it at the end of the function
    print(arr[size - 1], end = " ")
    leader = arr[size - 1]
    for i in range(size-2,-1,-1):
        if arr[i] >= leader :
            leader = arr[i]
            print(leader, end=" ")


if __name__ == '__main__':
    arr = [2,50,9,13,21,10,23,8,6,0,7,12,6,4]
    print('The leader element(s) : ')
    find_leaders(arr, len(arr))



