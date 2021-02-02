import random
import memory_profiler
from memory_profiler import profile

@profile
def sort_mylist():
    list = []
    for i in range(100):
        list.append(random.randrange(1, 1000, 1))

    print(list)

    # Sorting the list.
    list.sort()

    print("List Sorted: " +str(list))
sort_mylist()

x  = memory_profiler.memory_usage()

print(x[-1])