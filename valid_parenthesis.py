""" Given a string 's" containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input is valid.
An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type. """


def isvalid(s):
    # false if string has only one character = False
    if len(s) % 2 == 1:
        return False

    # starts with a closing character = False
    if s[0] == ")" or s[0] == "}" or s[0] == "]":
        return False

    stack = []
    # add opening brackets to stack, if closing bracket is found and corresponding opening bracket isn't found in stack
    # return False
    stack_peep = ""
    for item in s:
        if item == "(":
            stack.append(item)
        elif item == "{":
            stack.append(item)
        elif item == "[":
            stack.append(item)
        # if stack is empty and a closing bracket is used, return False
        elif item == ")" and len(stack) == 0:
            return False
        elif item == "}" and len(stack) == 0:
            return False
        elif item == "]" and len(stack) == 0:
            return False
        elif item == ")" and len(stack) != 0:
            stack_peep = stack.pop()    # pop top item off stack to check if it is a corresponding bracket
            if stack_peep != "(":       # push back to stack if not corresponding
                stack.append(stack_peep)
                return False
        elif item == "}" and len(stack) != 0:
            stack_peep = stack.pop()
            if stack_peep != "{":
                stack.append(stack_peep)
                return False
        elif item == "]" and len(stack) != 0:
            stack_peep = stack.pop()
            if stack_peep != "[":
                stack.append(stack_peep)
                return False
    # if stack cleared, means all corresponding brackets worked, not cleared means some unmatching brackets
    if len(stack) == 0:
        return True
    else:
        return False


