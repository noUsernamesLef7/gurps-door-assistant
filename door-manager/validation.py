def is_valid_boolean(user_input):
    if user_input == "True" or user_input == "False":
        return True
    else:
        print "Input must be 'True' or 'False'!"
        return False
       
def is_valid_number(user_input, allow_negative, allow_zero):
    try:
        int(user_input)
    except ValueError:
        print "Input must be a number!"
        return False
    if not allow_negative and int(user_input) < 0:
        print "Input cannot be negative!"
        return False
    if not allow_zero and int(user_input) == 0:
        print "Input cannot be 0!"
        return False
    else:
        return True


