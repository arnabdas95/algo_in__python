#from a given binary number sort the array as all the zero comes first
def binary_array_sorting(a,b):
    sum = 0
    for i in range(b+1):
        sum += int(a[i])
    sum =b+1-sum
    for i in range(sum):
        a[i] = 0


    for i in range (sum,b+1,1):
        a[i] = 1

def main():
    testcase = int(input())
    for x in range(testcase):
        length = int(input())
        arr = input().split()
        binary_array_sorting(arr,(len(arr)-1))
        print(arr)

if __name__ == '__main__':
   main()