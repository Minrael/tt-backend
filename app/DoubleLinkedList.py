import unittest

class Item():
    '''An element of list'''

    def __init__(self, elem, prev_item=None, next_item=None):
        self.elem = elem
        self.prev_item = prev_item
        self.next_item = next_item

class DoubleLinkedList():
    '''for sequence'''

    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last
        self.length = 0


    def push(self, elem):
        '''Add element at the end of the list'''
        new_item = Item(elem)
        self.length += 1
        if self.first is None:
            self.first = self.last = new_item
        else:
            new_item.prev_item = self.last
            new_item.next_item = None
            self.last.next_item = new_item
            self.last = new_item


    def pop(self):
        '''Delete element from the end of the list'''
        if self.first is None:
            print("List is already empty")
            return
        self.length -= 1
        if self.first is self.last:
            self.first=self.last=None
        else:
            self.last = self.last.prev_item
            self.last.next_item = None


    def unshift(self, elem):
        '''Add element at the beginning of the list'''
        new_item = Item(elem)
        if self.first is None:
            self.first = self.last = new_item
        else:
            new_item.prev_item = None
            new_item.next_item = self.first
            self.first.next_item = self.first
            self.first = new_item

    
    def shift(self):
        '''Delete element from the beginning of the list.'''
        if self.first is None:
            print("List is already empty")
        self.length -= 1
        if self.first.next_item is self.last:
            self.first = self.last = None
        else:
            self.first.prev_item = self.first
            self.first = self.first.next_item



    def len(self):
        '''Counting of lst's length.'''
        return self.length



    def delete(self, elem):
        '''Delete element from the list.'''
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



    def contains(self, elem):
        """Chacks that the lest contains the element."""
        ind_elem = self.first
        while (ind_elem.next_item is not None):
            if (ind_elem.elem is elem):
                return True
            else:
                ind_elem = ind_elem.next_item

            if ind_elem.next_item is None:
                print("element not found")
                return False


    def first():
        """Return the first element of the list"""
        return self.first.elem

    def last():
        """Return the last element of the list"""
        return self.last.elem

#Print all elements
#    def outputList(self):
#       index_item = self.first
#        while index_item is not None:
#           print index_item.elem
#           index_item = index_item.next_item


if __name__ == '__main__':

        list_1 = DoubleLinkedList()
        list_1.unshift(1)
        list_1.unshift(2)
        list_1.unshift(3)
        list_1.unshift(4)
        print(list_1.last())



