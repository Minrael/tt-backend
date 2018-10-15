import unittest
from app.DoubleLinkedList import DoubleLinkedList 

class TestDoubleLinkedList(unittest.TestCase):
    
    def test_emptyList(self):
        list_1 = DoubleLinkedList()
        self.assertEqual(list_1.first, None)

    def test_push(self):
        list_1 = DoubleLinkedList()
        list_1.push(1)
        self.assertEqual(list_1.last.elem, 1)

    def test_pop(self):
        list_1 = DoubleLinkedList()
        list_1.push(1)
        list_1.pop()
        self.assertEqual(list_1.len(), 0)

    def test_del(self):
        list_1 = DoubleLinkedList()
        list_1.push(1)
        list_1.push(2)
        list_1.push(2)
        list_1.delete(2)
        self.assertEqual(list_1.len(), 2)

    def test_len(self):
        list_1 = DoubleLinkedList()
        list_1.push(1)
        list_1.unshift(2)
        self.assertEqual(list_1.len(), 1)

    def test_contains_true(self):
        list_1 = DoubleLinkedList()
        list_1.push(1)
        list_1.push(2)
        list_1.push(3)
        list_1.push(4)
        self.assertEqual(list_1.contains(3), True)

    def test_contains_false(self):
        list_1 = DoubleLinkedList()
        list_1.push(1)
        list_1.push(2)
        list_1.push(3)
        self.assertEqual(list_1.contains(0), False)




if __name__ == '__main__':
	unittest.main()
