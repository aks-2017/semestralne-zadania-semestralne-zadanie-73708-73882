class Node:
    name = ""
    loc = ""
    category = ""

    def __init__(self, name, loc, category):
        self.name = name
        self.loc = loc
        self.category = category


def make_node(name, loc, category):
    node = Node(name, loc, category)
    return node

