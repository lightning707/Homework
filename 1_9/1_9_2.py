import json

attributes = ('telephone number', 'first name', 'last name', 'city or state')
with open("phonebook.json", "r") as file:
    records_lst = json.load(file)


def add_entity():
    dict_ = {}
    for attr in attributes:
        inp_ = input("Enter the " + attr + ': ')
        dict_.update({attr: inp_})
    records_lst.append(dict_)


def search_record(attr, value):
    for record in records_lst:
        if record[attr] == value:
            print(record)


def delete_record(value, attr_del="telephone number"):
    for record in records_lst:
        if record[attr_del] == value:
            records_lst.remove(record)


def update_record(value, attr_rm="telephone number"):
    dict_ = {attr_rm: value}
    attr_lst = list(attributes)
    attr_lst.remove(attr_rm)
    for record_idx in range(len(records_lst)):
        if records_lst[record_idx][attr_rm] == value:
            for attr in attr_lst:
                inp_ = input("Enter new " + attr + ": ")
                dict_.update({attr: inp_})
            records_lst[record_idx] = dict_


exit_flag = False
while not exit_flag:
    search_by = ""
    for i in range(len(attributes)):
        search_by += f"{i+4}: Search by {attributes[i]}\n"
    user_action = input("Press a number:\n" +
                        "1: Add a new record\n" +
                        "2: Delete a record for a telephone number\n" +
                        "3: Update a record for a telephone number\n" +
                        search_by +
                        "0: Exit the program\n")
    if user_action == "0":
        with open("phonebook.json", "w") as file:
            json.dump(records_lst, file, indent=4)
        exit(0)
    if user_action == "1":
        add_entity()
    if user_action == "2":
        inp = input("Enter the telephone number: \n")
        delete_record(inp)
    if user_action == "3":
        inp = input("Enter the telephone number: \n")
        update_record(inp)
    if user_action.isnumeric():
        if (int(user_action) >= 4) and (int(user_action) <= 4 + len(attributes)):
            inp = input(f"Enter the {attributes[int(user_action)-4]}: \n")
            search_record((attributes[int(user_action)-4]), inp)

with open("phonebook.json", "w") as file:
    json.dump(records_lst, file, indent=4)
