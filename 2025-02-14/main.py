# Python datatypes
# Snake-case: hello_world
age = 99                # int
rating = 4.5            # float
name = 'Jake'           # str
other_name = "Jake"     # str
is_paid = True          # bool
# empty_list_1 = []
# empty_list_2 = list()
# Age = 123
# agE = 123
attendance = {'Jake', 'Darlyn', 'Darlyn'}

games = ['COD', 'Valorant']   # list
games.append('FIFA 2025')
games.append('Hollow Knight')

shopping_cart = []
shopping_cart.append('bike')
shopping_cart.append('gloves')
shopping_cart.append('bond paper')

sample_set = {5, 2, 3, 4, 3, 4, 4}   # set
sample_set.add(63)
sample_set.add(0.2)

colors = ('red', 'green', 'blue', 123, True, 123)   # tuple

# print(colors)



number_list = [1, 2, 3]
number_set = {4, 5, 6}
number_tuple = (7, 8, 9)

# casting
# print(set(number_list))
# print(tuple(number_set))
# print(type(number_tuple))

user_info = ['jake', 'jake@gmail.com', 2356434, 987897, 'https://facebook.com/123456', 'http://mysite.com']
user_info = {
    'username': 'jake',
    'email': 'jake@gmail.com',
    'user_id': 2356434,
    'library_card_id': 987897,
}   # dict
user_info['high_score'] = 543674
del user_info['high_score']
# print(user_info)


empty_dict = {}     # empty dict
empty_set = set()   # empty set
empty_tuple = tuple()   # empty tuple

# print(empty_dict)


fruits = ['apple', 'banana', 'pear', 'apple']

# casting
print(list(set(fruits)))