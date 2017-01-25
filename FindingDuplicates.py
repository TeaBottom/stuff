# Given an array, how do you find all duplicates? The highest value and size of array are given.
# The values are all positive integers.

# Define arrays
numArray = [0, 0, 1, 3, 5, 5, 7, 7, 9, 5]
boolArray = [False, False, False, False, False, False, False, False, False, False]

for i in range(0, 10, 1):  # increment through array
    num = numArray[i]  # num becomes the value of the array at i
    if boolArray[num] == True:  # check if the loop has encountered the value of array[i]
        print numArray[i]  # print the duplicate
    boolArray[num] = True  # acknowledge that the array passed the value
