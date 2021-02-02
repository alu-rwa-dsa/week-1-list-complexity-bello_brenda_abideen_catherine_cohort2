import random
import time

def listcheck():
    # Creating the list
    list = []
    sort = time.time()
    for i in range(100):
        list.append(random.randrange(1, 100, 1))

    print(list)

    # Sorting the list.
    list.sort()
    # printing the last element
    print("Largest element in this list is:", list[-1])
    print("Time taken is ",time.time() - sort)


listcheck()
