def bubble_sort(list):
    unsorted_index = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_index):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
        unsorted_index -= 1
    return list
print(bubble_sort([1,6,4,5,74,3]))