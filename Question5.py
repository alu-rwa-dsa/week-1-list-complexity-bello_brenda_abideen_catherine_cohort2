from time import time
import Question3

# Estimate how long each algorithm would take for inputs of size 1,000,000.
# Algorithm 1

starting_time = time()
Question3.find_maximum([1])
ending_time = time()
time_difference = ending_time - starting_time
print("Time for input size 1: " + str(time_difference))
print("Time for input size 1,000,000: " + str(time_difference))

# Algorithm 2
starting_time1 = time()
Question3.make_lowercase("M")
ending_time1 = time()
time_difference1 = ending_time1 - starting_time1
print("Time for input size 1: " + str(time_difference1))
print("Time for input size 1,000,000: " + str(time_difference1))

# Algorithm 3
starting_time2 = time()
Question3.sort_list([1])
ending_time2 = time()
time_difference2 = ending_time2 - starting_time2
print("Time for input size 1: " + str(time_difference2))
print("Time for input size 1,000,000: " + str(time_difference2))
