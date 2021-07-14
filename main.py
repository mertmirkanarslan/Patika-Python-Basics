# First question is about flatten function.

print("Project Part 1 : Write a flatten function")
print("------------------------------------")
my_input = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5, [[[['dinosaur']]], 19]]
print("Our input is: " + str(my_input))
# We should create an empty list for flatten list.
EmptyList = []


def flatten(x):
    for i in x:
        if type(i) != list:
            EmptyList.append(i)
        else:
            flatten(i)
    return EmptyList


print("The result is:" + str(flatten(my_input)))
print("Part 1 is over.")


# Second question is about reversal list

print("Project Part 2 : Write a reverse function")
print("-------------------------------------------")

my_array = [[1, 2], 3, [4, 5], [6, 7, 8], [9, 10, [11, 12]], [14, 13, 20, [25, 16, [17, 33, 19]]]]
print("Our input array is:" + str(my_array))


def reverse_array(my_array):
    my_array.reverse()
    for arr in my_array:
        if(type(arr) == list):
            reverse_array(arr)


reverse_array(my_array)
reverse_array(my_input)
print("The result is:" + str(my_array))
print("We can try this function with the first question's input too:")
print("First Question's Result for Question 2 is:" + str(my_input))
print("Part 2 is over. Program is terminating...")