from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions, new_expense, get_expense_report, refound_debt
from user import add_user

def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","Show Status","New User"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
        ask_option()

    if (option['main_options']) == "New User":
        # print("Add new user")
        add_user()
        ask_option()
    if (option['main_options']) == "Show Status":
        # print("Show Status")
        get_expense_report()
        refound_debt()
        ask_option()

def main():
    ask_option()

main()