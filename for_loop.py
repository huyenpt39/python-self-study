'''
# There is a list of these elements: Hello, hi, Xin chao, Bye, Goodbye, See you
input_list = ["Hello", "hi", "Xin chao", "Bye", "Goodbye", "See you"]
# 1. Extract the first letter of each element from input list
# Hint:
expected_output1 = ["H", "h", "X", "B", "G", "S"]

# 2. Extract all element which starts with letter "H" or letter "S" from the input list
# Hint:
expected_output2 = ["Hello", "hi", "See you"]

# 3. Convert all elements of input list to lowercase
# Hint: use function lower(). For example: print("Hello".lower()) => output: hello
expected_output3 = ["hello", "hi", "xin chao", "bye", "goodbye", "see you"]
'''


def check_answer(actual, expected):
    if 'ellipsis' in str(type(actual)):
        print("Not completed")
        return

    assert actual == expected, "Your answer is wrong"
    print("Congratulation! You did a good job!")


input_list = ["Hello", "hi", "Xin chao", "Bye", "Goodbye", "See you"]

# 1.
# put your code here
print("+Task 1:")
actual_ouput1 = []
for x in input_list:
    actual_ouput1.append(x[0])
print(actual_ouput1)

check_answer(actual_ouput1, ["H", "h", "X", "B", "G", "S"])

# 2.
# put your code here
print("+Task 2: ")
actual_output2 = []
for x in input_list:
    if x[0]=='H' or x[0]=='h' or x[0]=='S':
        actual_output2.append(x)
print(actual_output2)
check_answer(actual_output2, ["Hello", "hi", "See you"])

# 3.
# put your code here
print("+Task 3: ")
actual_output3 = []
for x in input_list:
    actual_output3.append(x.lower())
print (actual_output3)
check_answer(actual_output3, ["hello", "hi", "xin chao", "bye", "goodbye", "see you"])


