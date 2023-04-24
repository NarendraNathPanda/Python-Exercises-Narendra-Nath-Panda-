users = {'001': 'Shreyasree', '002': 'Shreya', '003': 'Swarnali'}
user_id = '004'

try:
    print(users[user_id])
except KeyError:
    print(f'The {user_id} key is not in the dictionary. Adding key ...')
    users[user_id] = None
print(users)