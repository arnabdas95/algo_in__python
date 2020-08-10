'''Fibonacci series using DYNAMIC PROGRAMMING .
Yeild is used here for memeory optimization.it only store the next value not all the values'''
import cProfile
def fibonacci_series(n):

    if(n<0):
        print("No fibonacci series for Negetive number!!")
        return
    a = 0
    b = 1
    for i in range(n):
        yield a
        a , b = b , a + b

if __name__ == '__main__':

    for number in fibonacci_series(10):
        print(number)

    print("In a list form as it is a generator class")
    cProfile.run('print(list(fibonacci_series(1000)))')


'''
RECURSION require much more time

def fibo(n):
  if(n<0):
        print("No fibonacci series for Negetive number!!")
        return
  if n == 1:
      return 1;
  if n == 0:
      return  0;
  else:
      return fibo(n-1)+fibo(n-2)


result = fibo(40)
print(result)'''
