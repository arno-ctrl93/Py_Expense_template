import csv


def post_new_user(name):
    with open('users.csv', 'a', newline='') as csvfile:
        fieldnames = ['name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'name': name})
        return True

def fetch_user():
    with open('users.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        users = []
        for row in reader:
            users.append(row['Name'])
        # print(users)
        return users