import unittest
import phonebook
import json

# attributes = ('telephone number', 'first name',
# 'last name', 'city or state')


class TestPhonebook(unittest.TestCase):
    def setUp(self):
        with open('phonebook.json', 'w') as fd:
            json.dump([{"telephone number": 1234567, "first name": "Dmytro", "last name": "A", "city or state": "Kyiv"}], fd)
        self.phonebook = phonebook.Phonebook()

    def test_add_entity(self):
        with open('phonebook.json', 'w') as fd:
            json.dump([], fd)
        self.phonebook.records_lst = []
        self.phonebook.add_entity(1234567, 'Dmytro', 'A', 'Kyiv')
        file_read = []
        with open('phonebook.json', 'r') as fd:
            file_read = json.load(fd)
        self.assertEqual([{"telephone number": 1234567, "first name": "Dmytro", "last name": "A", "city or state": "Kyiv"}], file_read)

    def test_search_phone_number(self):
        self.assertEqual(self.phonebook.search_record("telephone number", 1234567), {"telephone number": 1234567, "first name": "Dmytro", "last name": "A", "city or state": "Kyiv"})

    def test_delete_record(self):
        self.phonebook.delete_record("first name", "Dmytro")
        with open('phonebook.json', 'r') as fd:
            res = json.load(fd)
        self.assertEqual(res, [])

    def tearDown(self) -> None:
        with open('phonebook.json', 'w') as fd:
            json.dump([], fd)


if __name__ == '__main__':
    unittest.main()
