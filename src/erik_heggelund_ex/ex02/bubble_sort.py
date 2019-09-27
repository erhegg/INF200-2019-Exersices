def bubble_sort(list_to_be_sorted):
    """The function takes a list or tuple and sorts it with the bubble sort method.
    The function returns the sorted list or tuple as a tuple.
    """
    sorted_list = list(list_to_be_sorted)
    for iteration_number in range(1, len(list_to_be_sorted)):
        for index in range(len(sorted_list[:-iteration_number])):
            if sorted_list[index] > sorted_list[index+1]:
                sorted_list[index], sorted_list[index+1] \
                    = sorted_list[index+1], sorted_list[index]
            else:
                pass
    return tuple(sorted_list)


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
