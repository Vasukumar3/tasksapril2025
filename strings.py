# Creating strings
# single_quoted_string = 'Hello, World!'
# double_quoted_string = "Python String's"
# triple_quoted_string = '''Triple quotes allow
# strings to span multiple lines.'''
# print(single_quoted_string)
# print(double_quoted_string)
# print(triple_quoted_string)

# sample = str()
# print(type(sample))

# sample_2 = ""
# print(type(sample_2))

# my_string = "Python@123" #indexing
# # seq[index]
# print(my_string[6]) #@
# print(my_string[-4]) #@
# print(my_string[0]) #P
# print(my_string[-10]) #P
# print(my_string[9]) # -1
# print(my_string[-1]) # -1


# sample = "python life"
# print(sample[1:6])
# print(sample[10:6:-1])

# message = "Hello, World!"
# upper_con= message.upper()
# print(upper_con)
# print(message)


# message = "Hello, World!@123"
# low_con = message.lower()
# print(low_con)

# sentence = "This is a sample sentence."
# count_i = sentence.count('e')
# print(count_i)


# whitespace_string = "   This is a string with leading and trailing whitespace.   "
# print(len(whitespace_string))
# stripped_string = whitespace_string.strip()
# print(stripped_string)


data = "Pythonlife,Kiran,123456"
data1 = data.split(',')
print(data1)


# original_string = "Python is fun!"
# modified_string = original_string.replace('Python', 'pythonlife')
# print(modified_string) 


# filename = "example.txt"
# starts_with = filename.startswith("ex")
# ends_with = filename.endswith(".txt")
# print(starts_with) 
# print(ends_with)  








# email_list = ["example1@gmail.com", "example2@yahoo.com", "example3@gmail.com", "example4@hotmail.com","example5@outlook.com"]
# new_list = []
# for i in email_list:
#     if i.endswith("@gmail.com"):
#         new_list.append(i)
# print(new_list)

# [exp for item in iter if cond]
# result = [i for i in email_list if i.endswith("@yahoo.com")]
# print(result)

# print([i for i in email_list if i.endswith("@yahoo.com")])


# sentence = "This is a sentence."
# position_a = sentence.find('z')
# position_i = sentence.index('z')
# print(position_a)  
# print(position_i) 


# text = "python programming"
# capitalized_text = text.capitalize()
# print(capitalized_text)


# numeric_string = "12345"
# alpha_string = "Python"

# is_numeric = numeric_string.isdigit()
# is_alpha = alpha_string.isalpha()

# print(is_numeric)  
# print(is_alpha)   


word_list = ['Hello', 'World']
joined_string = ' '.join(word_list)

print(joined_string) 