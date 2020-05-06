import pyfiglet

global contact
count = 0


def main():
    # Start up banner
    ascii_banner = pyfiglet.figlet_format('Contact\nManagement\nSystem', font='chunky')
    print(ascii_banner)

    # Get current count of contacts
    file = open('my_contacts.txt', 'r')
    for x in file:
        if "Last Name: " in x:
            global count
            count = count + 1

    while True:
        start = input('You currently have ' + str(count) + ' contacts. Would you like to add a new contact?: '
                                                           '(y) (n)')
        if start.lower() == 'y':
            add_contact()
        elif start.lower() == 'n':
            print('Have a great day! Goodbye!')
            exit()
        else:
            print('Please enter y or n!')


def add_contact():
    while True:
        first_name = input('First Name: ')
        if not first_name:
            print('First name is required. ')
        else:
            middle_name = input('Middle Name: (optional)')
            while True:
                last_name = input('Last Name: ')
                if not last_name:
                    print('Last name is required. ')
                else:
                    while True:
                        address1 = input('Address1: ')
                        if not address1:
                            print('Address1 is required.')
                        else:
                            address2 = input('Address2: (optional)')
                            phone = input('Telephone Number: (optional)')
                            global contact
                            contact = 'First Name: ' + first_name + '\n' + \
                                      'Middle Name: ' + middle_name + '\n' + \
                                      'Last Name: ' + last_name + '\n' + \
                                      'Address 1: ' + address1 + '\n' + \
                                      'Address 2: ' + address2 + '\n' + \
                                      'Telephone Number: ' + phone + '\n\n'
                            save_contact()


def save_contact():
    file = open('my_contacts.txt', 'a')
    file.write(contact)
    file.close()
    global count
    count = count + 1

    while True:
        another = input('Your contact has been saved! You now have ' + str(count) + ' contacts. Would you '
                                                                                    'like to save another? (y) '
                                                                                    '(n) ')
        if another.lower() == 'y':
            add_contact()
        elif another.lower() == 'n':
            print('Have a great day! Goodbye!')
            exit()
        else:
            print('Please enter y or n!')


main()
