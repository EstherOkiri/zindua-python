#=====importing libraries===========
'''This is the section where you will import libraries'''

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''
login_info = {}

def register_user(new_username,new_password):
    login_info[new_username] = new_password
    print (login_info)
    with open('user.txt', 'r') as users :
        for line in users:
            details = line.strip().split(", ")
            username = details[0]
            password = details[1]
            login_info[username] = password

input_username = input("Enter username:  ")
input_password = input("Password: ")

for user_info in login_info:
    while input_username == username and input_password == password:
        # Present the menu to the user and make sure that the user input is converted to lower case.
        print("Tasks You Can Do.")
        print("r - register a user, a - add task , va - view all tasks, vm - view my tasks, e - exit")
        menu = input("Select a task you want to do: ").lower
        
        if menu == 'r':
            new_username = input("Enter username : ").lower
            new_password = input("Enter account password : ").lower
            confirm_password = input("Enter account password again : ").lower
            if confirm_password == new_password :
                register_user(new_username,new_password)



          