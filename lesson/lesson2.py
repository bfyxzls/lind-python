my_int = 42
my_float = 3.14
my_complex = 1 + 2j
my_string = "Hello, World!"
print(len(my_string))
print(my_string.lower())
print(my_string.upper())
print(my_string.split(","))

my_bool_true = True
my_bool_false = False
print("my_bool_false", my_bool_false)

my_list = [1, 2, 3, 'four', 5.0]
my_list.append(6)
my_list.remove(1)  # set集合中，第1个元素的索引是1，这与数组不同
print(my_list)

my_tuple = (1, 2, 3)
first_element = my_tuple[0]
print("first_element", first_element)

my_set = {1, 2, 3, 4}
my_set.add(5)
my_set.remove(2)
print(my_set)
for set in my_set:
    print(set)

my_dict = {'name': 'Alice', 'age': 25}
print(my_dict['name'])
for dict in my_dict.items():
    print(dict)
