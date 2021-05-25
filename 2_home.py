def user_inf(name, surname, state, birthday, number, mail):
    return f'Name: {name} Surname: {surname} Birthday: {birthday} City: {state} E-mail: {mail} Telephone: {number}'


your_name = input('Enter your Name: ')
your_surname = input('Enter your Surname: ')
your_birthday = input('Enter your Birthday: ')
your_city = input('Enter your City: ')
your_mail = input('Enter your E-mail: ')
your_number = input('Enter your Telephone number: ')

print(user_inf(your_name, your_surname, your_birthday, your_city, your_number, your_mail))
