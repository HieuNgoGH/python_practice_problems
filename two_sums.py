"""Given an array of integers 'nums' and an integer 'target', return the indices of the two numbers such that they add up to the 'target'."""

def twoSum(nums, target):
    target_list = []
    counter = 0
    counter2 = 1
    while counter < len(nums):
        while counter2 < len(nums):
            if nums[counter] + nums[counter2] == target:
                target_list.append(counter)
                target_list.append(counter2)
                return target_list
            else:
                counter2 += 1
        counter += 1
        counter2 = counter + 1

    return target_list


#nums = [3, 2, 4]
#target = 6
#print(twoSum(nums, target))
