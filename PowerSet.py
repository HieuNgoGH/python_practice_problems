import copy

def powerset_helper(pointer, choices_made, input, result):
    result1 = []
    if (pointer < 0):
        result1 = copy.copy(choices_made)
        result.append(result1)
        return result

    choices_made.append(input[pointer])
    powerset_helper(pointer-1, choices_made, input, result)
    #backtracking
    choices_made.pop()
    powerset_helper(pointer-1, choices_made, input, result)

def powerset(input):
    result = []
    powerset_helper(len(input)-1, [], input, result)
    return result

#nums = [1,2,3]
#print(powerset(nums))
