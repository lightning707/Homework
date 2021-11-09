import unittest
import mymod


class MymodTest(unittest.TestCase):
    def setUp(self) -> None:
        self.test = mymod.test

    def test_numbers(self):
        with open("file1.txt", "w") as file:
            file.write("123456789")
        self.assertEqual(self.test('file1.txt'), (1, 9))

    def test_symbols(self):
        with open("file1.txt", "w") as file:
            file.write("@#$%&^()*")
        self.assertEqual(self.test('file1.txt'), (1, 9))

    def test_letters(self):
        with open("file1.txt", "w") as file:
            file.write("qwerty")
        self.assertEqual(self.test('file1.txt'), (1, 6))

    def test_lines(self):
        with open("file1.txt", "w") as file:
            file.write("qwerty\n12345")
        self.assertEqual(self.test('file1.txt'), (2, 12))

    def test_no_path(self):
        from sys import path
        path.remove("/home/andrew/PycharmProjects/python_project/Homework/2_19/2_19_3")
        with open("file1.txt", "w") as file:
            file.write("qwerty\n12345")
        self.assertEqual(self.test('file1.txt'), (2, 12))
