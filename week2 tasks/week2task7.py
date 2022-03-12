def make_account():
    """function to make an account"""
    name = input('Enter your name: (separate by space) ')
    try:
        name = name.split(' ')  # split name to be list
        first_name = name[0][0]  # get first index (first name) and first letter from it.
        last_name = name[1]
        account = first_name + '.' + last_name
        return account
    except:  # if name not correct return false
        return False


print('***Welcome to our program***')
accounts = []
num_of_accounts = input('Enter number of account you want to create: ')
try:
    num_of_accounts = eval(num_of_accounts)
    while num_of_accounts > 0:
        account = make_account()
        if account:
            accounts.append(account)
        else:
            print('Invalid input')
        num_of_accounts -= 1
except:
    print('Please enter a valid number!')

print('Accounts:\n')
for account in accounts:
    print(account.swapcase())  # to convert capital to small and vice versa.