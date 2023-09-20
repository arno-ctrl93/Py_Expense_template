from PyInquirer import prompt
from expenseReportRepository import post_new_expense, fetch_expense
from userRepository import fetch_user


def fill_expense_questions():
    users = fetch_user()
    expense_questions[2]['choices'] = users
    return True

def fill_payback_expense_questions(userBuyer):
    users = fetch_user()
    multipleChoiceUsers = []
    for user in users:
        if (user != userBuyer):
            multipleChoiceUsers.append({'name':user})
    payback_expense_questions[0]['choices'] = multipleChoiceUsers
    return True

def fill_refound():
    users = fetch_user()
    refund_questions[1]['choices'] = users
    return True


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": []
    },

]

payback_expense_questions = [   
    {
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'New Expense - Paybacks: ',
        'name': 'paybacks',
        'choices': [],
        'validate': lambda answer: 'You must choose at least one paybacks.'
            if len(answer) == 0 else True
    },
]




def new_expense(*args):
    # print("Expense - New Expense")
    if (fill_expense_questions() == False):
        print("Error while fetching users")
        return False
    infos = prompt(expense_questions)
    # print(infos)
    if (fill_payback_expense_questions(infos['spender']) == False):
        print("Error while fetching users")
        return False
    paybacks = prompt(payback_expense_questions)
    # print(paybacks)
    post_new_expense(infos['amount'],infos['label'],infos['spender'], paybacks['paybacks'])
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    # print("Expense Added !")
    return True

    

def get_expense_report():
    users = fetch_user()
    print("Il y a " + str(len(users)) + " utilisateurs: ")
    for user in users:
        print(user)
    print("=== Voici les dettes actuelles ===")
    expenses = fetch_expense()
    matrix = []
    for r in range(0, len(users)):
        matrix.append([0 for c in range(0, len(users))])
    for expense in expenses:
        spender = expense['Spender']
        payback = expense['Payback']
        spenderindex = users.index(spender)
        paybackindex = users.index(payback)
        amount = float(expense['Amount'])
        # print( "spenderindex: " + str(spenderindex) + " paybackindex: " + str(paybackindex) + " amount: " + str(amount))
        matrix[spenderindex][paybackindex] += amount
    # print(matrix)

    # Affichage des dettes
    for i in range(len(users)):
        for j in range(len(users)):
            if matrix[i][j] > 0:
                if matrix[j][i] > 0:
                    difference = matrix[i][j] - matrix[j][i]
                    if difference > 0:
                        print(f"{users[j]} doit {difference} euros à {users[i]}")
                else:
                    print(f"{users[j]} doit {matrix[i][j]} euros à {users[i]}")

    # print(matrix)

refund_questions = [
    {
        "type":"list",
        "name":"user",
        "message":"Who are you?",
        "choices": []
    }
]

def fill_refound_user_questions():
    users = fetch_user()
    refound_user_questions[0]['choices'] = users
    return True

refound_user_questions = [
    {
        "type":"list",
        "name":"refoundUser",
        "message":"Which user do you want to refund?",
        "choices": []
    },
]


def refound_debt():
    fill_refound()
    type_of_refund = prompt(refund_questions)
    if (type_of_refund['whichRefound']) == "Refund a person":
        print("Refund a person")
        # TODO
    if (type_of_refund['whichRefound']) == "Refund for an expense":
        print("Refund for an expense")
        # TODO
    return