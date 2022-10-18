""" STACK """


class Stack:
    """Stack degan class yaratildi"""

    def __init__(self):
        """class ning list  degan atrebuti"""
        self.list = []

    def isEmpty(self):
        """ Bo`sh ekanligini tekshirish """
        return len(self.list) == 0

    def push(self, data):
        """ Element qo`shish """
        self.list.append(data)
        print(f'# {data} pushed to stack__')

    def pop(self):
        """ Element sug`irib olish """
        # if self.isEmpty():
        #     print('# stack is empty')
        #     return
        tmp = self.list.pop()
        print(f'# {tmp} popped from stack__')
        return tmp

    def peek(self):
        """ Eng ustki elementni ko`rish """
        if self.isEmpty():
            return " Steck is empty"
        else:
            return self.list[-1]


""" stack degan obyekt olindi Stack classidan """
stack = Stack()
stack.push(5)
stack.push('salom')

stack.pop()
stack.pop()
stack.pop()
print(stack.list)

""" --> MISOL <-- """

# class Stack:
#     def __init__(self):
#         self.list = []
#
#     def push(self, data):
#         self.list.append(data)
#         print(f'# {data} pushed to stack__')
#
#     def pop(self):
#         if self.isEmpty():
#             print('# stack is empty')
#             return
#         tmp = self.list.pop()
#         print(f'# {tmp} popped from stack__')
#         return tmp
#
#     def peek(self):
#         if self.isEmpty():
#             print('# stack is empty')
#             return
#         return self.list[-1]
#
#     def isEmpty(self):
#         return len(self.list) == 0
#
#
# stack = Stack()
# s1 = input().split()
# print(s1)
# for i in s1:
#     if i.isdigit():
#         stack.push(int(i))
#     elif i == '+':
#         a = stack.pop()
#         b = stack.pop()
#         stack.push(a + b)
#     elif i == '-':
#         a = stack.pop()
#         b = stack.pop()
#         stack.push(b - a)
#     elif i == '*':
#         a = stack.pop()
#         b = stack.pop()
#         stack.push(a * b)
#     elif i == '/':
#         a = stack.pop()
#         b = stack.pop()
#         stack.push(b / a)
#     elif i == '=':
#         print(stack.peek())

""" Faqat harflarni o`zini saqlay oladi """

# class Stack:
#     def __init__(self):
#         self.list = []
#
#     def push(self, data):
#         self.list.append(data)
#         print(f'# {data} pushed to stack__')
#
#     def pop(self):
#         if self.isEmpty():
#             print('# stack is empty')
#             return
#         tmp = self.list.pop()
#         print(f'# {tmp} popped from stack__')
#         return tmp
#
#     def top(self):
#         if self.isEmpty():
#             print('# stack is empty')
#             return
#         return self.list[-1]
#
#     def isEmpty(self):
#         return len(self.list) == 0
#
#
# stack = Stack()
# s1 = input().split()
# print(s1)
# for i in s1:
#     if i.isdigit():
#         continue
#     else:
#         stack.push(i)
# print(stack.list)
