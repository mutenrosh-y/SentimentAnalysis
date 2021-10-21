from p1 import *
from collections import namedtuple

credential = namedtuple('credential', ['login_id', 'password'])
reg_cred = namedtuple('reg_cred', ['name', 'email', 'password'])
#def make_user_credential(login_id: str, password: str):
    #return credential[login_id, password]

def get_login_creds():
    login_id = input("Enter Login ID: ")
    password = input("Enter Password: ")
    entered_cred = credential(login_id, password)
    return entered_cred

def check_id(entered_cred, id):
    return entered_cred.login_id == id 

def check_password(entered_cred, password):
    return entered_cred.password == password

def cross_ref_users_table():
    entered_cred = get_login_creds()
    users = pd.read_csv('UsersTable.csv')
    output = "Wrong Password"
    count_iter = 0
    for id, password in zip(users['Login ID'], users['Password']):
        if check_id(entered_cred, id):
            if check_password(entered_cred, password):
                return True
            
        if check_password(entered_cred, id):
            if not check_id(entered_cred, id):
                output = "Wrong ID"
        count_iter += 1
    
    if count_iter == len(users['Login ID']):
        output += " and Wrong ID"
    print(output)
    return False

def check_yes(key):
    return key == 'Y' or key == 'y'

def get_input(required: str):
    return input("Enter " + required + ": ")

def get_user_registered():
    user_name = get_input("name")
    user_email = get_input("email")
    reg_password = get_input("password")
    return reg_cred(user_name, user_email, reg_password)

def registration():
    entered_reg_cred = get_user_registered()
    #add_to_csv()
    #re_login()

def send_email():
    pass

def add_to_csv():
    pass

def re_login():
    pass

def login():
    for i in range(3):
        print("Attempt ", i+1)
        if cross_ref_users_table():
            print(f'Login Successful')
            return True
        else:
            print("Login Unsuccessful")
            register_ft_user_key = input("Do you wish to register (Y/n)?")
            if check_yes(register_ft_user_key):
                return registration()
            else:
                continue

    forgot_key = input("Attempts Over, Have you forgotten your password(Y/n)?")
    if check_yes(forgot_key):
        return send_email()
    return False

login()