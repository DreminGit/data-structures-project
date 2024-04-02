"""Пишем тесты используя  ЮЮнитест"""
import unittest
from src.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.top.data, 1)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)


    def test_repr(self):
        stack = Stack()
        self.assertEqual(str(stack), "Стак данных")



if __name__ == '__main__':
    unittest.main()