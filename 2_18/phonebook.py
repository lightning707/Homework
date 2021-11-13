import json

attributes = ('telephone number', 'first name', 'last name', 'city or state')


class Phonebook:
    def __init__(self):
        with open("phonebook.json", "r") as file:
            self.records_lst = json.load(file)

    def add_entity(self, *args):
        dict_ = {}
        for i in range(len(attributes)):
            dict_.update({attributes[i]: args[i]})
        self.records_lst.append(dict_)
        with open("phonebook.json", "w") as file:
            json.dump(self.records_lst, file)

    def search_record(self, attr, value):
        for record in self.records_lst:
            if record[attr] == value:
                return record

    def delete_record(self, attr_del, value):
        for record in self.records_lst:
            if record[attr_del] == value:
                self.records_lst.remove(record)
        with open("phonebook.json", "w") as file:
            json.dump(self.records_lst, file)

    def update_record(self, value, attr_rm="telephone number"):
        dict_ = {attr_rm: value}
        attr_lst = list(attributes)
        attr_lst.remove(attr_rm)
        for record_idx in range(len(self.records_lst)):
            if self.records_lst[record_idx][attr_rm] == value:
                for attr in attr_lst:
                    inp_ = input("Enter new " + attr + ": ")
                    dict_.update({attr: inp_})
                self.records_lst[record_idx] = dict_

    def run(self):
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
                    json.dump(self.records_lst, file, indent=4)
                exit(0)
            if user_action == "1":
                self.add_entity()
            if user_action == "2":
                inp = input("Enter the telephone number: \n")
                self.delete_record(inp)
            if user_action == "3":
                inp = input("Enter the telephone number: \n")
                self.update_record(inp)
            if user_action.isnumeric():
                if (int(user_action) >= 4) and (int(user_action) <= 4 + len(attributes)):
                    inp = input(f"Enter the {attributes[int(user_action)-4]}: \n")
                    self.search_record((attributes[int(user_action)-4]), inp)
