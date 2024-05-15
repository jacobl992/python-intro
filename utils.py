def find_max(numbers):
    max = 0
    for number in numbers:
        if number > max:
            max = number
            #we are overwrting the built in Python function of 'max' which is bad practise, but just doing this to complete the exercise
    return max