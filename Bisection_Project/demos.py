import time
from random import choice
from string import ascii_lowercase as letters


# Bisection Implementation 

def bisection_sort(email, arr):
    start = 0
    stop = len(arr) - 1
    while start <= stop:
        mid = (start + stop) // 2
        if email == arr[mid]:
            return mid, f"{email} found at index: {mid}"
        elif email > arr[mid]:
            start = mid + 1
        else:
            stop = mid - 1

    return None, f"{email} not found"

# Function to execution time

def analyzer(f,*args):
    tic = time.time()
    f(*args) 
    toc = time.time()
    seconds = toc - tic
    print(f"{f.__name__.capitalize()}\t-> Elapsed time: {seconds:.9f} ")

### Functions for generating lists ###

def generate_name(length_of_name):
    return ''.join(choice(letters) for i in range(length_of_name))

def generate_emails(length_of_name, list_of_domains, total_emails):
    emails = []
    for i in range(total_emails):
        emails.append(generate_name(length_of_name) + choice(list_of_domains))
    return emails
