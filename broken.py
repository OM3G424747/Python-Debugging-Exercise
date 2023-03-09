def quick_sort(numbers):
    quick_sort_helper(numbers, 0, len(numbers)-1)


def quick_sort_helper(numbers, first, last):
    if first < last:
        splitpoint = partition(numbers, first, last)

        quick_sort_helper(numbers, first, splitpoint - 1)
        quick_sort_helper(numbers, splitpoint + 1, last)


def partition(numbers, first, last):
    pivotvalue = numbers[last]

    rightmark = first
    leftmark = first

    while rightmark <= last:

        if numbers[rightmark] > pivotvalue:
            rightmark += 1

        else:
            temp = numbers[rightmark]
            numbers[rightmark] = numbers[leftmark]
            numbers[leftmark] = temp
            rightmark += 1
            leftmark += 1

    return leftmark - 1


numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Before Sort: {}".format(numbers))
quick_sort(numbers)
print("After Sort: {}".format(numbers))

# Change log:
# Updated indentation to increments of 4 spaces to correct indentation
# Removed two while loops due to them resulting in marker instantly being moved all the way to the right
# Moved logic to update rightmarker in if statement
# Updated marker initial values to both start at zero and then increment
# Refactored existing while loop to rather check the current position of the rightmark
# Fixed logical error from incorrect pivot being returned
# Updated logic in else statement to move both markers if a value has been swapped
# Updated marker naming switched left and right marker naming to switch them arround
