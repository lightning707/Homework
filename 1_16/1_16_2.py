class Boss:
    def __init__(self, id_, name, company):
        self.id = id_
        self.name = name
        self.company = company
        self._worker_lst = []

    def __str__(self):
        return f"Name: {self.name} | " \
               f"id: {self.id} | " \
               f"Company: {self.company}"

    @property
    def boss(self):
        return self

    @boss.setter
    def boss(self, new):
        if type(new) == Boss:
            self.id = new.id
            self.name = new.name
            self.company = new.company
            self._worker_lst = new.workers

    @property
    def workers(self):
        return self._worker_lst

    @workers.setter
    def workers(self, new_workers):
        new_lst = []
        for person in new_workers:
            if type(person) == Boss:
                new_lst.append(person)
        return new_lst


class Worker:
    def __init__(self, id_, name, company, boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    def __str__(self):
        return f"Name: {self.name} | " \
               f"id: {self.id} | " \
               f"Company: {self.company} "

    def __repr__(self):
        return f"Name: {self.name} | " \
               f"id: {self.id} | " \
               f"Company: {self.company} "


boss1 = Boss(5, "Andrew", "Valve")
print(boss1.boss)
boss1.boss = Boss(3, "Boris", "McDonalds")
print(boss1.boss)
boss1.workers.append(Worker(6, "Vlad", "Google", boss1))
boss1.workers.append(Worker(11, "Misha", "Google", boss1))
print(boss1.workers)
