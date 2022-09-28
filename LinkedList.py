""" Linked List """

# class Node:
#     """Tugun (node) obyekti"""
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     """Linked List obyekti"""
#     def __init__(self):
#         self.head = None




"""Linked list yaratib olamiz"""
# llist = LinkedList()

"""3 ta node (tugun) yaratamiz"""
# llist.head = Node('Dushanba')
# tuesday = Node('Seshanba')
# wednesday = Node('Chorshanba')

"""Tugunlar hali bog`lanmagan"""
# print(llist.head.data)
# print(tuesday.data)

"""Tugunlarni bog`lab chiqamiz"""
# llist.head.next = tuesday
# tuesday.next = wednesday
#
# print(llist.head.data)
# print(llist.head.next)
# print(llist.head.next.data)
# print(llist.head.next.next.data)


class Node:
    """Tugun (node) obyekti"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Linked List obyekti"""
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        """Listni boshidan tugun qo`shish"""
        # Yangi node yaratamiz
        new_data = Node(new_data)
        # Listni boshini keyingi o`ringa suramiz
        new_data.next = self.head
        # Yangi nodeni list boshiga qo`yamiz
        self.head = new_data

    def insertAfter(self, prev_node, new_data):
        """Birorta tugundan so`ng tugun qo`shish"""
        if prev_node is None:
            print("Tugun mavjud emas")
            return
        # Yangi tugun qo`shamiz
        new_node = Node(new_data)
        # Yangi tugunni keyingi tugunga bog`laymiz
        new_node.next = prev_node.next
        # Avvalgi tugunni yangi tugunga bog`laymiz
        prev_node.next = new_node

    def append(self, new_data):
        """List oxiriga tugun qo`shish"""
        # Yangi tugun yaratamiz
        new_node = Node(new_data)
        # List bo`sh emasligini tekshiramiz
        if self.head is None:
            # Bo`sh bo`lsa yangi tuggun list boshiga qo`shiladi
            self.head = new_node
            return
        # Akis xolda list oxiriga boramiz
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def deleteNode(self, key):
        """Listdan qiymat o`chirish"""
        # List boshini topib olamiz
        temp = self.head
        # Birinchi tuguni tekshiramiz
        if (temp and temp.data == key):
            self.head = temp.next
            temp = None
            return
        # Aks holda keyingi tugunlarni qarab chiqiladi
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # Agar qiymat topilmasa
        if temp == None:
            return
        # Tugunni listdan o`chiramiz
        prev.next = temp.next
        temp = None


"""Linked list yaratib olamiz"""
llist = LinkedList()

"""3 ta node (tugun) yaratamiz"""
llist.head = Node('Dushanba')
tuesday = Node('Seshanba')
wednesday = Node('Chorshanba')

"""Linked List konsolga chiqarish"""
 llist.printList()

"""List boshiga yangi tugun qo`shamiz"""
llist.push('Yakshanba')
 llist.printList()

""" List o`rtasidan element qo`shamiz """
 llist.insertAfter(llist.head.next, 'Dushanba kechasi')
 llist.printList()

"""List oxiriga tugun qo`shamiz"""
llist.append('Payshanba')
 llist.printList()

"""Listdan element o`chirish"""
llist.deleteNode('Chorshanba')
llist.printList()

