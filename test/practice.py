#practice.py
import copy

class ListNode:
    def __init__(self, value, child = None):
        self.value = value
        self.child = child

class stack:
    base_node = None
    min_array = []

    class stackNode:
        def __init__(self, value, child = None):
            assert(type(value) == int)
            self.value = value
            self.child = child

    def is_empty(self):
        return self.base_node == None

    def pop(self):
        if self.base_node == None:
            raise Exception
        if self.base_node.child == None:
            return_node = self.base_node
            self.base_node = None
            self.min_array = []
            return return_node
        else:
            current_node = self.base_node.child
            previous_node = self.base_node
            while current_node.child != None:
                temp = current_node
                current_node = current_node.child
                previous_node = temp
            previous_node.child = None
            # if current_node.value == self.min_array[-1]:
            #     self.min_array = self.min_array[:-1]
            return current_node

    def peek(self):
        if self.base_node == None:
            raise Exception
        if self.base_node.child == None:
            return self.base_node
        else:
            current_node = self.base_node.child
            while current_node.child != None:
                current_node = current_node.child
            return current_node

    def push(self, value):
        if type(value) == int:
            node = self.stackNode(value)
        else:
            node = value
        if self.base_node == None:
            self.base_node = node
            self.min_array.append(value)
        else:
            current_node = self.base_node
            while current_node.child != None:
                current_node = current_node.child
            current_node.child = node
            # if node.value < self.min_array[-1]:
            #     self.min_array.append(value)

    def min(self):
        return self.min_array[-1]

class MyQueue:
    stack1 = stack()
    stack2 = stack()

    def push(self, value):
        if self.stack2.is_empty():
            self.stack1.push(value)
        else:
            while not self.stack2.is_empty():
                self.stack1.push(self.stack2.pop())
            self.stack1.push(value)
    def peek(self):
        if not self.stack2.is_empty():
            return self.stack2.peek()
        if not self.stack1.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
            return self.stack2.peek()
    def pop(self):
        if not self.stack2.is_empty():
            return self.stack2.pop()
        if not self.stack1.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()


class LinkedList:
    first_node = None

    class listNode:
        def __init__(self, value, child = None):
            self.value = value
            self.child = child

    def append(self, value):
        if self.first_node == None:
            self.first_node = self.listNode(value)
        else:
            current_node = self.first_node
            while current_node.child != None:
                current_node = current_node.child
            current_node.child = self.listNode(value)


def remove_dups(list):
    first_node = list.first_node
    if first_node.child != None:
        values_seen = set()
        second_node = first_node.child
        values_seen.add(first_node.value)
        while second_node != None:
            if second_node.value in values_seen:
                first_node.child = second_node.child
                second_node = first_node.child
            else:
                values_seen.add(second_node.value)
                temp = second_node
                second_node = second_node.child
                first_node = temp

def kthLast(list1, k):
    runner = list1.first_node
    for x in range(k):
        if runner.child == None:
            raise Exception
        else:
            runner = runner.child
    first_node = list1.first_node
    while runner.child != None:
        runner = runner.child
        first_node = first_node.child
    return first_node.value

def delete_middle(node):
    pointer = node
    if pointer.child == None:
        pointer = None
    while pointer.child.child != None:
        pointer.value = pointer.child.value
        pointer = pointer.child
    pointer.value = pointer.child.value
    pointer.child = None

def partition(list1, partition):
    front_node = list1.first_node
    first_node = list1.first_node
    second_node = first_node.child
    while second_node != None:
        if second_node.value < partition:
            temp = second_node.child
            second_node.child = front_node
            front_node = second_node
            first_node.child = temp
            second_node = temp
        else:
            temp = second_node
            second_node = second_node.child
            first_node = temp
    list1.first_node = front_node

def is_palindrome(list1):
    array1 = []
    current_node = list1.first_node
    while current_node != None:
        array1.append(current_node.value)
        current_node = current_node.child
    array2 = array1[:]
    
    while array1 != []:
        if array1.pop() != array2.pop(0):
            return False
    return True

def is_unique(string):
    my_set = set()
    for x in range(len(string)):
        if string[x] in my_set:
            return False
        else:
            my_set.add(string[x])
    return True

def is_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    dict1 = {}
    dict2 = {}
    for x in range(len(string1)):
        if string1[x] in dict1:
            dict1[string1[x]] += 1
        else:
            dict1[string1[x]] = 1
        if string2[x] in dict2:
            dict2[string2[x]] += 1
        else:
            dict2[string2[x]] = 1
    return dict1 == dict2

def is_palindrome_permutation(string):
    seen_odd_key = False
    my_dict = {}
    for x in range(len(string)):
        if string[x] in my_dict:
            my_dict[string[x]] += 1
        else:
            my_dict[string[x]] = 1
    for key in my_dict.keys():
        if my_dict[key]%2 != 0:
            if seen_odd_key == False:
                seen_odd_key = True
            else:
                return False
    return True

def one_away(string1, string2):

    #remove or insert
    if len(string1) - len(string2) == 1 or len(string1) - len(string2) == -1:
        longer_string = (string1 if len(string1)>len(string2) else string2)
        shorter_string = (string1 if longer_string == string2 else string2)
        for x in range(len(longer_string)):
            if longer_string[:x] + longer_string[x+1:] == shorter_string:
                return True

    #replace
    if len(string1) == len(string2):
        for x in range(len(string1)):
            if string1[:x] + string1[x+1:] == string2[:x] + string2[x+1:]:
                return True
    return False

def string_compression(string):
    output_string = ''
    current_type = string[0]
    current_count = 1
    for x in range(1,len(string)):
        if string[x] == current_type:
            current_count += 1
        else:
            output_string += current_type + str(current_count)
            current_type = string[x]
            current_count = 1
        if x == len(string)-1:
            output_string += current_type + str(current_count)
    return (output_string if len(output_string)<len(string) else string)

class TreeNode:
    def __init__(self, value, left_child = None, right_child = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def min_tree(my_list):
    if my_list == []:
        return None
    middle_index = int(len(my_list)/2)
    root = TreeNode(my_list[middle_index])
    root.left_child = min_tree(my_list[:middle_index])
    root.right_child = min_tree(my_list[middle_index+1:])
    return root

def list_of_depths(root):
    output_array = [[root.value]]
    i = 0
    while list_of_depths1(root.left_child, i) + list_of_depths1(root.right_child, i) != []:
        output_array.append(list_of_depths1(root.left_child, i) + list_of_depths1(root.right_child, i))
        i += 1
    return output_array

def list_of_depths1(root, i):
    if root == None:
        return []
    if i == 0:
        return [root.value]
    else:
        return list_of_depths1(root.left_child, i-1) + list_of_depths1(root.right_child, i-1)


def check_balanced(root):
    if root.left_child == None and root.right_child == None:
        return True
    if root.left_child == None and root.right_child != None:
        if root.right_child.right_child != None or root.right_child.left_child != None:
            return False
        else:
            return check_balanced(root.right_child)
    if root.left_child != None and root.right_child == None:
        if root.left_child.right_child != None or root.left_child.left_child != None:
            return False
        else:
            return check_balanced(root.left_child)
    else:
        return check_balanced(root.left_child) and check_balanced(root.right_child)

def validate_BST(root):
    if root == None:
        return True
    if root.left_child != None and root.left_child.value > root.value:
        return False
    if root.right_child != None and root.right_child.value < root.value:
        return False
    return validate_BST(root.left_child) and validate_BST(root.right_child)

class Project:
    def __init__(self, title, dependencies):
        self.title = title
        self.dependencies = dependencies

def first_common_ancestor(root, node1, node2):
    if root == node1 or root == node2:
        return root
    if is_in_tree(root.right_child, node1) and is_in_tree(root.right_child, node2):
        return first_common_ancestor(root.right_child, node1, node2)
    if is_in_tree(root.left_child, node1) and is_in_tree(root.left_child, node2):
        return first_common_ancestor(root.left_child, node1, node2)
    return root


def is_in_tree(root, node):
    if root == None:
        return False
    if root == node:
        return True
    return is_in_tree(root.left_child, node) or is_in_tree(root.right_child, node)

def syr(n):
    if n == 1:
        return 0
    if n%2 == 0:
        return 1 + syr(n/2)
    else:
        return 1 + syr(n*3+1)

def sortedMerge(list1, list2):
    i = 0
    j = 0
    while i < len(list1):
        if list1[i] > list1[j]:
            temp = list1[i]
            list1[i] = list2[j]
            list2[j] = temp
            bubble(list2)
        i += 1
    list1 += list2
    return list1

def bubble(list1):
    i = 0
    while i < len(list1) - 1 and list1[i] > list1[i+1]:
        temp = list1[i]
        list1[i] = list1[i+1]
        list1[i+1] = temp
        i += 1

def group_anagrams(list1):
    list_of_dictionaries = []
    for x in list1:
        x = ''.join(sorted(x))
        i = 0
        dict1 = {}
        while i < len(x):
            if x[i] in dict1.keys():
                dict1[x[i]] += 1
            else:
                dict1[x[i]] = 1
            i += 1
        list_of_dictionaries.append(str(dict1))
    dictionary_of_dictionaries = {}
    for x in list_of_dictionaries:
        if str(x) in dictionary_of_dictionaries.keys():
            dictionary_of_dictionaries[x] += 1
        else:
            dictionary_of_dictionaries[str(x)] = 1
    print(dictionary_of_dictionaries)
    output_list = []
    for x in dictionary_of_dictionaries.keys():
        if dictionary_of_dictionaries[x] > 1:
            index_list = []
            i = 0
            while i < len(list_of_dictionaries):
                if list_of_dictionaries[i] == x:
                    index_list.append(i)
                i += 1
            for x in index_list:
                output_list.append(list1[x])
    for x in list1:
        if x not in output_list:
            output_list.append(x)
    return output_list

class wrapper:
    def __init__(self, value, index):
        self.value = value
        self.index = index

def remove_parens(my_string):
    string_length = len(my_string)
    parens_stack = []
    other_stack = []
    for x in range(len(my_string)):
        if my_string[x] == '(' or my_string[x] == ')':
            parens_stack.append(wrapper(my_string[x],x))
        else:
            other_stack.append(wrapper(my_string[x],x))
    burn_indices = clean_stack(parens_stack)
    output_string = ''
    for x in range(string_length):
        if x not in burn_indices:
            if parens_stack != [] and parens_stack[0].index == x:
                output_string += parens_stack.pop(0).value
            else:
                output_string += other_stack.pop(0).value
    return output_string

def clean_stack(my_list):
    burn_list = []
    burn_indices = []
    current_sum = 0
    for x in range(len(my_list)):
        if my_list[x].value == '(':
            current_sum += 1
        elif current_sum <= 0:
            burn_list.append(my_list[x].index)
            burn_indices.append(x)
            current_sum -= 1
        else:
            current_sum -= 1
    used_indices = []
    for x in range(len(my_list)-1, 0, -1):
        if my_list[x].value == '(' and x not in used_indices and current_sum > 0:
            burn_indices.append(x)
            burn_list.append(my_list.pop(x).index)
            used_indices.append(x)
            current_sum -= 1
    for x in burn_indices:
        my_list = my_list[:x] + my_list[x+1:]
    
    return burn_list

def gamma(x):
    if x == 1:
        return 1
    return (x-1)*gamma(x-1)

def math(my_string):
    is_simple = True
    for x in ['+', '-', '*', '/']:
        if x in my_string:
            is_simple = False
    if is_simple:
        return int(my_string)
    left = my_string[0]
    i = 1
    while my_string[i] not in ['+', '-', '*', '/']:
        left += my_string[i]
        i += 1
    if my_string[i] == "+":
        return int(left) + math(my_string[i+1:])
    if my_string[i] == "-":
        return int(left) - math(my_string[i+1:])
    if my_string[i] == "*":
        right = ""
        i += 1
        while i < len(my_string) and my_string[i] not in ['+', '-', '*', '/']:
            right += my_string[i]
            i += 1
        if i == len(my_string):
            return int(left) * int(right)
        if my_string[i] == '+':
            return int(left) * int(right) + math(my_string[i+1:])
        if my_string[i] == '-':
            return int(left) * int(right) - math(my_string[i+1:])
        if my_string[i] == '*':
            return int(left) * int(right) * math(my_string[i+1:])
        if my_string[i] == '/':
            return int(left) * int(right) / math(my_string[i+1:])
    if my_string[i] == "/":
        right = ""
        i += 1
        while i < len(my_string) and my_string[i] not in ['+', '-', '*', '/']:
            right += my_string[i]
            i += 1
        if i == len(my_string):
            return int(left) / int(right)
        if my_string[i] == '+':
            return int(left) / int(right) + math(my_string[i+1:])
        if my_string[i] == '-':
            return int(left) / int(right) - math(my_string[i+1:])
        if my_string[i] == '*':
            return int(left) / int(right) * math(my_string[i+1:])
        if my_string[i] == '/':
            return int(left) / int(right) / math(my_string[i+1:])

def make_valid(my_string):
    if my_string == "":
        return my_string
    while my_string[0] != '(' or my_string[-1] != ")":
        if my_string[0] == ')':
            my_string = my_string[1:]
        if my_string[-1] == '(':
            my_string = my_string[:-1] 
        if my_string == "":
            return my_string
    count = 0
    for x in range(len(my_string)):
        if my_string[x] == '(':
            count += 1
        else:
            count -= 1
    if count > 0:
        i = len(my_string)-1
        while count != 0:
            if my_string[i] == "(":
                my_string = my_string[:i] + my_string[i+1:]
                count -= 1
            i -= 1
        return my_string


    if count < 0:
        i = 0
        while count != 0:
            if my_string[i] == ")":
                my_string = my_string[:i] + my_string[i+1:]
                count += 1
            i += 1
        return my_string

    return my_string

def make_valid2(my_string):
    burn_indices = []
    stack = []
    i = 0
    while i < len(my_string):
        if my_string[i] == '(':
            stack.append(i)
        elif stack == []:
            burn_indices.append(i)
        else:
            stack.pop()
        i += 1
    burn_indices += stack
    burn_indices = sorted(burn_indices, reverse=True)
    for x in burn_indices:
        my_string = my_string[:x] + my_string[x+1:]
    return my_string

def math_parens(my_string):
    stack = []
    i = 0
    while i < len(my_string):
        if my_string[i] != ')':
            stack.append(my_string[i])
        else:
            equation = ""
            while stack[-1] != '(':
                equation = stack.pop() + equation
            stack.pop()
            stack.append(str(math(equation)))
        i += 1
    print(''.join(stack))
    return math(''.join(stack))

def savage_facebook(my_string):
    standard_array = []
    bracket_array = []
    for i in range(len(my_string)):
        if my_string[i] in ['(', ')']:
            bracket_array.append((i, my_string[i]))
        else:
            standard_array.append((i, my_string[i]))
    stack = []
    kept_brackets = []
    for x in bracket_array:
        if x[1] == '(':
            stack.append(x)
        elif stack != []:
            kept_brackets.append(stack.pop())
            kept_brackets.append(x)
    kept_brackets.sort(key = lambda tup: tup[0])
    output_string = ""
    while standard_array != [] or kept_brackets != []:
        if standard_array != [] and kept_brackets != []:
            if standard_array[0][0] < kept_brackets[0][0]:
                output_string += standard_array[0][1]
                standard_array.pop(0)
            else:
                output_string += kept_brackets[0][1]
                kept_brackets.pop(0)
        if standard_array != []:
            output_string += standard_array.pop(0)[1]
        else:
            output_string += kept_brackets.pop(0)[1]
    return output_string

def increment_array(array1):
    for x in range(len(array1)):
        array1[x] += 1

def permutations(array1, num, set):
    if num < min(array1):
        return 0
    for x in array1:
        if num - x == 0:
            total += 1
        elif num - x > 0:
            total += permutations(array1, num - x)
    return total

def fb(my_string):
    my_stack = []
    my_set = set()
    for x in range(len(my_string)):
        if my_string[x] == '(':
            my_stack.append((x,'('))
        if my_string[x] == ')' and my_stack != []:
            my_set.add(x)
            my_set.add(my_stack.pop()[0])
    output_array = []
    for x in range(len(my_string)):
        if my_string[x] not in ['(', ')'] or x in my_set:
            output_array.append(my_string[x])
    return ''.join(output_array)

def removeDuplicates(A):
    i = 0
    while i < len(A) -1:
        if A[i] == A[i+1]:
            A = A[:i] + A[i+1:]
        else:
            i += 1
    return A
                

def preOrder(t):
    if t == None:
        return []
    else:
        return [t.value] + preOrder(t.left_child) + preOrder(t.right_child) 

def facebook(string):
    stack = []
    my_set = set()
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(i)
        if string[i] == ')' and stack != []:
            my_set.add(i)
            my_set.add(stack.pop())
    output = ''
    for i in range(len(string)):
        if string[i] not in [')', '('] or i in my_set:
            output += string[i]
    return output

def evaluate(string):
    stack = []
    op_seen = False
    for i in range(len(string)):
        if op_seen:
            if string[i] in ['+', '-', '*', '/']:
                first = ''
                second = ''
                while stack[-1] not in ['*', '/']:
                    second = stack.pop() + second
                operator = stack.pop()
                while stack != [] and stack[-1] not in ['*', '/', '+', '-']:
                    first = stack.pop() + first
                if operator == '*':
                    stack.append(str(int(first)*int(second)))
                    op_seen = False
                else:
                    stack.append(str(int(first)/int(second)))
                    op_seen = False
            else:
                stack.append(string[i])
        else:
            if string[i] in ['*', '/']:
                op_seen = True
            stack.append(string[i])
    print(stack)
    op_seen = False
    left = ''
    right = ''
    op = ''
    done = False
    while not done:
        if op_seen:
            if stack [-1] in ['+', '-'] or len(stack) == 1:
                if op == '+':
                    stack.append(str(int(left)+str(right)))
                else:
                    stack.append(str(int(left)-str(right)))
                op_seen = False
            else:
                left = stack.pop() + left
        else:
            if stack[-1] in ['+', '-']:
                op_seen = True
                op = stack.pop()
            else:
                right = stack.pop() + right
    return int(stack[0])






        



            












