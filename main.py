#list comprehension
# fruits = ["apples", "bananas", "strawberries"]
# new_fruits = []

# for fruit in fruits:
#   fruit = fruit.upper()
#   new_fruits.append(fruit)
  
# fruits = new_fruits
# print(fruits)


# fruits = ["apples", "bananas", "strawberries"]
# fruits = [fruit.upper() for fruit in fruits]

# print(fruits)




# conditionals 
# bits = [False, True, False, False, True, False, False, True]
# new_bits = []

# for b in bits:
#   if b == True:
#     new_bits.append(1)
#   else:
#     new_bits.append(0)

# super_bits = [1 if b == True else 0 for b in bits]

# print(bits)
# print(new_bits)
# print(super_bits)




#string manipulation
# my_string = "HelloMyNameIsMariya"
# my_string = ''.join(
#   [i if i.islower() else " " + i.lower() if i in ["N", "I"] else " " + i for i in my_string]
# )[1:]
# print(my_string)


word_list = [letter if letter in used_letter else '-' for letter in word]
print('Current word:', ' '.join(word_list))

for letter in word:
  if letter in use_letter:
    print(letter)
  else: 
    print("-")
