from random import randint
import time
from sorting_algos import quicksort, mergesort, selection_sort, bubble_sort

#Function to generate lists of a certain size 

def list_generator(size,max):
    list = []
    [list.append(randint(0,max)) for x in range(size)]
    return list

#Function to determine time elapse of sorting the list using the specified algorithm
def time_elapsed(f,arr):
    tic = time.time()
    f(arr)
    toc = time.time()
    seconds = toc - tic
    print(f"{f.__name__.capitalize()}\t-> Elapsed time: {seconds:.5f} ")


#User Input
size = int(input("What size of list do you want to create? "))
max = int(input("What is the max value of the range? "))
num_of_runs = int(input("How many times do you want to run this? "))

l = list_generator(size,max)


#Time Elapse for Different Algorithms
if size * max < 10000:

    for num in range(num_of_runs):
        print(f"Run: {num + 1}")
        time_elapsed(quicksort,l)
        time_elapsed(mergesort,l)
        time_elapsed(selection_sort,l.copy())
        time_elapsed(bubble_sort,l.copy())
        time_elapsed(__builtins__.sorted,l)
        print("-" * 40)
else:

    for num in range(num_of_runs):
        time_elapsed(quicksort,l)
        time_elapsed(mergesort,l)
        time_elapsed(__builtins__.sorted,l)






# __name__ gives the name of the function rather than the string representation
