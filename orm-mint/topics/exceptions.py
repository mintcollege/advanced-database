user_info = {
    'username': 'jake'
}


# try:
#     # print(user_info['email'])
#     user = await session.get(Account, 1)
#     print('All is fine')
# # except KeyError:
# #     print('User cannot be found.')
# except Exception:
#     print('Something happened but I do not know what')

# try:
#     raise ValueError('Wrong value')
#     raise KeyError('You shall not pass!')
# except Exception as e:
#     print(e)

# def access_fictional_db():
#     try:
#         data = access_database_1()
#         return data
#     except Exception as e:
#         try:
#             data = access_database_2()
#             return data
#         except Exception as e:
#             return 'Cannot access your data at this time. Try again in a few seconds.'
#
# data = access_fictional_db()


def a():
    raise ValueError('You did something wrong here, buddy.')
    # try:
    # except Exception as e:
    #     return 1223

def b():
    a()
    # try:
    # except Exception as e:
    #     return 123

# try:
#     b()
# except Exception as e:
#     print('You are wrong.')

# b()

# def type_age(age: int):
#     if not isinstance(age, int):
#         raise ValueError('Only integers are allowed.')
#     print(age)
#
#
# type_age('123')


# raise Exception()
# try:
# except (ValueError, KeyError) as e:
#     print('Bad')
# # except KeyError as e:
# #     print('Bad')
# except Exception as e:
#     pass
# # finally:
# #     print('This will run whether there is an error or not')
#
#
#
#



class CannotApplyDeathPenalty(Exception):
    # error_code: int | None = None
    #
    # def __init__(self, message):
    #     self.error_code = 404
    pass

try:
    raise CannotApplyDeathPenalty('This person has already been released.')
except Exception as e:
    print(e.error_code)



