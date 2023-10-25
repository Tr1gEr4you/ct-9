class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def pop(self, index):
        if index < 0 or index >= self.size():
            raise IndexError("Index out of range")

        if index == 0:
            data = self.head.data
            self.head = self.head.next
            return data

        current = self.head
        for i in range(index - 1):
            current = current.next
        data = current.next.data
        current.next = current.next.next
        return data

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Пример использования
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print("Список после добавления элементов:", linked_list.display())
print("Размер списка:", linked_list.size())

linked_list.remove(2)
print("Список после удаления элемента 2:", linked_list.display())

popped_value = linked_list.pop(1)
print("Извлеченное значение по индексу 1:", popped_value)
print("Список после извлечения:", linked_list.display())