# --------- #
# Recursion #
# --------- #

# 1. Write a function that uses recursion to print each item in a list.
def print_item(my_list, i=0):
    """Prints each item in a list recursively.

    >>> print_item([1, 2, 3])
    1
    2
    3

    >>> print_item([])

    """
    if i < len(my_list):
        print(my_list[i])
        print_item(my_list, i+1)

    # if len(my_list) > 1:
    #     print(my_list[i])
    #     print_item(my_list[1:])
    # elif len(my_list) == 1:
    #     print(my_list[i])


# 2. Write a function that uses recursion to print each node in a tree.


def print_all_tree_data(tree):
    """Prints all of the nodes in a tree.


    >>> class Node:
    ...     def __init__(self, data):
    ...             self.data=data
    ...             self.children = []
    ...     def add_child(self, obj):
    ...             self.children.append(obj)
    ...
    >>> one = Node(1)
    >>> two = Node(2)
    >>> three = Node(3)
    >>> one.add_child(two)
    >>> one.add_child(three)
    >>> print_all_tree_data(one)
    1
    2
    3

    """
    print(tree.data)
    if tree.children:
        for child in tree.children:
            print_all_tree_data(child)


# 3. Write a function that uses recursion to find the length of a list.


def list_length(my_list):
    """Returns the length of list recursively.
    >>> list_length([1, 2, 3, 4])
    4

    """
    if not my_list:
        return 0
    
    return 1 + list_length(my_list[1:])
   

# 4. Write a function that uses recursion to count how many nodes are in a tree.


def num_nodes(tree):
    """Counts the number of nodes.

    >>> class Node:
    ...     def __init__(self, data):
    ...             self.data=data
    ...             self.children = []
    ...     def add_child(self, obj):
    ...             self.children.append(obj)
    ...
    >>> one = Node(1)
    >>> two = Node(2)
    >>> three = Node(3)
    >>> one.add_child(two)
    >>> one.add_child(three)
    >>> num_nodes(one)
    3
    >>> four = Node(4)
    >>> five = Node(5)
    >>> two.add_child(four)
    >>> two.add_child(five)
    >>> num_nodes(one)
    5
    >>> six = Node(6)
    >>> three.add_child(six)
    >>> num_nodes(one)
    6
    """

    if tree.children:
        nodecount = 1
        for child in tree.children:
            nodecount += num_nodes(child)
        return nodecount
    else:
        return 1
        

#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()
