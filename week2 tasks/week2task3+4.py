from datetime import datetime


def options(date):
    """function that returns date by display many options"""
    print(
        'Choose option:\n1- (Day number-Month name-Year number)\n2- (Day name-Month name-Year number)\n3- (Day number-Month number-Year number)')
    option = input(': ')

    if option == '1':
        return date.strftime('%d/%B/%Y')
    elif option == '2':
        return date.strftime('%A, %B %Y')
    elif option == '3':
        return date.strftime('%m %d %Y')
    else:
        return 'Please Enter a valid number!'


def date_to_text():
    """function to take date from user and make sure is valid"""

    date = input('Enter date to convert (in DD/MM/YYYY): ')
    try:
        # convert the date to datetime object
        dt_obj = datetime.strptime(date, '%m/%d/%Y').date()
        print(options(dt_obj))
    except:  # if date was wrong print a error message
        print('Please Enter a valid date!')


date_to_text()