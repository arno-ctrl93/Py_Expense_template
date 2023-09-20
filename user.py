from PyInquirer import prompt
from userRepository import post_new_user

user_questions = [
{
    "type":"input",
    "name":"name",
    "message":"New User - Name: ",
},
]

def add_user():
    # print("User - Add User")
    userInfos = prompt(user_questions)
    # print(userInfos)
    post_new_user(userInfos['name'])
    # print("User Added !")
    # This function should create a new user, asking for its name
    return