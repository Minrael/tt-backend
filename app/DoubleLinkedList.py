import unittest

class Item():

    def __init__(self, elem, prev_item=None, next_item=None):
        self.elem = elem
        self.prev_item = prev_item
        self.next_item = next_item

class DoubleLinkedList():

    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last
        self.length = 0

#Add element at the end of the list
    def push(self, elem):
        new_item = Item(elem)
        self.length += 1
        if self.first is None:
            self.first = self.last = new_item
        else:
            new_item.prev_item = self.last
            new_item.next_item = None
            self.last.next_item = new_item
            self.last = new_item

#Delete element from the end of the list
    def pop(self):
        if self.first is None:
            print("List is already empty")
            return
        self.length -= 1
        if self.first is self.last:
            self.first = self.last = None
        else:
            self.last = self.last.prev_item
            self.last.next_item = None

#Add element at the beginning of the list
    def unshift(self, elem):
        new_item = Item(elem)
        if self.first is None:
            self.first = self.last = new_item
        else:
            new_item.prev_item = None
            new_item.next_item = self.first
            self.first.next_item = self.first
            self.first = new_item

#Delete element from the beginning of the list
    def shift(self):
        if self.first is None:
            print("List is already empty")
            return
        self.length -= 1
        if self.first.next_item is self.last:
            self.first = self.last = None
        else:
            self.first.prev_item = self.first
            self.first = self.first.next_item


#Counting of lst's length
    def len(self):
        return self.length


#Delete element from the list
    def delete(self, elem):
        ind_elem = self.first
        while (ind_elem.next_item is not None):
            if (ind_elem.elem is not elem):
                ind_elem = ind_elem.next_item
            else:
                print("deleted")
            self.length -= 1
            if ind_elem is self.first:
                self.shift()
                break
            elif ind_elem is self.last:
                self.pop()
                break
            else:
                ind_elem.prev_item.next_item = ind_elem.next_item
                ind_elem.next_item.prev_item = ind_elem.prev_item
                break

            if ind_elem.next_item is None:
                print("element not found")


#Chacks that the lest contains the element
    def contains(self, elem):
        ind_elem = self.first
        while (ind_elem.next_item is not None):
            if (ind_elem.elem is elem):
                return True
            else:
                ind_elem = ind_elem.next_item

            if ind_elem.next_item is None:
                print("element not found")
                return False

#Return the first element of the list
    def first():
        return self.first.elem
#Return the last element of the list
    def last():
        return self.last.elem

#Print all elements
#    def outputList(self):
#       index_item = self.first
#        while index_item is not None:
#           print index_item.elem
#           index_item = index_item.next_item


if __name__ == '__main__':

        list_1 = DoubleLinkedList()
        list_1.push(1)
        list_1.push(2)
        list_1.first()



