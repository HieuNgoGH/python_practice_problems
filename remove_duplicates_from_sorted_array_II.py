"""Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique
element appears at most twice. The relative order of the elements should be kept the same.Since it
is impossible to change the length of the array in some languages, you must instead have the result be placed in the
first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k
elements of nums should hold the final result. It does not matter what you leave beyond the first k elements. Return k
after placing the final result in the first k slots of nums. Do not allocate extra space for another array. You must do
this by modifying the input array in-place with O(1) extra memory."""

def remove_duplicates(nums):

    k = 0
    if len(nums) == 0:      # if array has no elements return k as 0
        return k

    two_counter = 0
    counter = 0
    dynamic_range = len(nums)   # the range to check for duplicates gets smaller by 1 after a duplicate has been deleted
    while counter < dynamic_range:
        if counter == dynamic_range - 1:    # adds 1 to k and return to prevent out of range error
            k += 1
            return k
        elif nums[counter] == nums[counter + 1]:
            two_counter += 1
            if two_counter >= 2:                    # if two numbers equal as past 2 equals, remove the duplicate
                nums.remove(nums[counter + 1])
                two_counter -= 1                    # reduce duplicate counter by 1 and check next just in case same duplicate
                counter -= 1              # reduce element counter by 1 to stay in one place and check next number after removal
                k -= 1              # reduce k by 1 since number removed
                dynamic_range -= 1  # reduce range by 1 because of removal
            counter += 1
            if counter == dynamic_range:    # exits program to prevent out of range
                return k
            else:
                k += 1
        else:
            two_counter = 0
            if counter == dynamic_range:
                return k
            else:
                k += 1
                counter += 1

