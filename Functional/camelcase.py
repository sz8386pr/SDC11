from functools import reduce

user_input = input('Please enter the text to camelize: ')

input_list = user_input.split(' ')  # need to turn into a list to work with map/reduce... etc
all_lower =list(map(lambda x: x.lower(), input_list))   # lowercase them all
first_letter_cap = list(map(lambda x: x.capitalize(), all_lower))   # capitalize the first letter
joined = reduce(lambda a, b: a + b, first_letter_cap)   # join them back together
print('''
    CamelizedWord: {}

    The original input was \"{}\".
    Input was split per word into a list: {}
    they were turned to all lowercase: {}
    and then capitalized the first letter of each word: {}
    and finally joined them together into a single string \"{}\"'''
    .format(joined, user_input, input_list, all_lower, first_letter_cap, joined)
    )
