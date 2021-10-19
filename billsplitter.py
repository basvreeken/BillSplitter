import random

# write your code here

print('Enter the number of friends joining (including you):')
number_of_users = int(input())

if number_of_users <= 0:
    print('No one is joining for the party')
else:

    user_dictionary = dict()
    print('Enter the name of every friend (including you) each on a new '
          'line: ')
    count = number_of_users
    while count > 0:
        user = input()
        user_dictionary[user] = 0
        count -= 1

    print('Enter the total bill value:')
    total_bill = int(input())
    split_value = round(total_bill / number_of_users, 2)
    for k, v in user_dictionary.items():
        user_dictionary[k] = split_value

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    use_lucky = input()
    if use_lucky == "Yes":
        user_list = [k for k in user_dictionary]
        lucky = user_list[random.randint(1, number_of_users)]
        print(f'{lucky} is the lucky one!')

        # Calculate new splits
        split_value = round(total_bill / (number_of_users - 1), 2)
        for k, v in user_dictionary.items():
            user_dictionary[k] = split_value
        user_dictionary[lucky] = 0

    else:
        print('No one is going to be lucky')

    print(user_dictionary)
