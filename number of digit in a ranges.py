import cProfile
def no_of_occurence(num):
    sum = 0
    for i in range(num):
         while(i>0):
            if i%10 == 2:
                sum +=1
            i = i//10
    return sum


cProfile.run('print(no_of_occurence(99968))')