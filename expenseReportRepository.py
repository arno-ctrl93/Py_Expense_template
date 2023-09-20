import csv


def post_new_expense(amount, label, spender, paybacks):
    with open('expense_report.csv', 'a', newline='') as csvfile:
        fieldnames = ['Amount', 'Label', 'Spender', 'Payback', 'Refound']
        nbPaybacks = len(paybacks) + 1
        dividedAmount = float(amount) / nbPaybacks
        for payback in paybacks:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Amount': dividedAmount, 'Label': label, 'Spender': spender, 'Payback': payback, 'Refound': False})
        return True


def fetch_expense():
    with open('expense_report.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        expenses = []
        for row in reader:
            expenses.append(row)
        #print(expenses)
        return expenses

def update_expense_refound(refoundname, refoundername):
    expenses = fetch_expense()
    with open('expense_report.csv', 'w', newline='') as csvfile:
        fieldnames = ['Amount', 'Label', 'Spender', 'Payback', 'Refound']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for row in reader:
            if row['Payback'] == refoundname and row['Spender'] == refoundername:
                row['Refound'] = True
            if row['Payback'] == refoundername and row['Spender'] == refoundname:
                row['Refound'] = True
            writer.writerow(row)