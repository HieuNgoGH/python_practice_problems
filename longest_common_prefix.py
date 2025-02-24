
# Write a function to find the longest common prefix amongst an array of strings
def longest_common_prefix(array):

    items_in_array = (len(array))

    # find the string with the lowest amount of characters
    least_item_size = len(array[0])
    for item in array:
        if len(item) < least_item_size:
            least_item_size = len(item)

    items_in_array_constant = items_in_array
    item_size_constant = least_item_size
    item_prefix = ""
    items_in_array = len(array)

    # if there's only 1 item in array, that item is the longest common prefix
    if len(array) == 1:
        item_prefix = array[0]
        return item_prefix

    # return black if array has nothing in it
    if least_item_size == 0:
        return item_prefix

    while items_in_array > 1:
        if (array[items_in_array_constant - items_in_array][item_size_constant - least_item_size] ==
                array[items_in_array_constant - (items_in_array - 1)][item_size_constant - least_item_size]):
            items_in_array -= 1
            if items_in_array == 1:
                item_prefix += array[items_in_array_constant - items_in_array][item_size_constant - least_item_size]
                least_item_size -= 1
                if least_item_size == 0:
                    return item_prefix
                items_in_array = items_in_array_constant
        else:
            break

    print(item_prefix)
    return item_prefix


sample_array = ["ab", "a"]
print(longest_common_prefix(sample_array))

