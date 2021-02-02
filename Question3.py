# Algorithm 1
# Algorithm to generate the maximum number from a list
print("Algorithm 1:")

def find_maximum(array):
    max_num = 0
    for num in array:
        if num > max_num:
            max_num = num
    return max_num

numbers = [3198, 7298, 8762, 154, 724, 8765, 9875, 987, 3345, 9845]

print("Maximum number: " + str(find_maximum(numbers)))


# Algorithm 2
print("")
print("Algorithm 2:")
# Algorithm that makes each letter in a list lowercase
def make_lowercase(word):
    small_word = word.lower()
    return small_word

name = "CATHERINE"

print(make_lowercase(name))

# Algorithm 3
print("")
print("Algorithm 3:")
# Algorithm that sorts a list of integers
def sort_list(array):
    ordered_list = sorted(array)
    return ordered_list

num_list = [3, 7, 87, 15, 72]

print(sort_list(numbers))