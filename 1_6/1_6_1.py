input_str = input("Enter a sentence: ")

input_str = input_str.split()

result_dict = {}
for word in input_str:
    word_count = input_str.count(word)
    result_dict.update({word: word_count})

print(result_dict)
