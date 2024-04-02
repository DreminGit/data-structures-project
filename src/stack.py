class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.data = None
        self.stack = []
        self.top = None

    def __repr__(self):
        return f'{self.__class__.__name__}()'

    def __str__(self):
        return f'стак данных'

    def push(self, data) -> None:
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top


    def pop(self):
        """
        удаляет элемент с вершины и возвращает
        """
        pop = self.stack.pop()
        return pop

