# Rotate ana array in kth position clockwise
import cProfile
'''
TESTCASE INPUT
no of test case
length of test case array1 k
array
length of test case array2 k
array
...
OUTPUT
resultend arr1
resultend arr2
'''

"""
FIRST APPROCH
def rortae_clockwise(arr,k,l):
    left=k
    right=l-1
    while left<=right:
        arr[left] , arr[right] = arr[right], arr[left]
        left+=1
        right-=1

testcase = int(input())

for x in range(testcase):
    l,k = input().split()
    l= int(l)
    k= int (k)
    arr = input().split()
    rortae_clockwise(arr, 0, k)
    rortae_clockwise(arr, k, l)
    rortae_clockwise(arr, 0, l)
    print(arr)
"""


#2nd approch
#function to rotate element
def rotate_array(arr,k,l):
    temp_arr = []
    for i in range(k,l):
        temp_arr.append(arr[i])
    for i in range(k):
        temp_arr.append(arr[i])

    arr = temp_arr
    for i in range(l):
        print(arr[i],end=" ")
    print("\n")

#main program
if __name__ == '__main__':
    testcase = int(input())
    for x in range(testcase):
        l,k = input().split()
        arr = input().split()
        cProfile.run('rotate_array(arr,int(k),int(l))')


