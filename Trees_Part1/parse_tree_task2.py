import operator
from typing import Generic, TypeVar, List

from oop_tree import BinaryTree
from split_function import my_splits_bool

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container  # not is true for empty container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()  # LIFO

    def __repr__(self) -> str:
        return repr(self._container)


def build_parse_tree(math_exp: str) -> BinaryTree:
    tokens_list = my_splits_bool(math_exp)
    stack = Stack()
    tree: BinaryTree = BinaryTree('')
    stack.push(tree)
    current_tree = tree
    print(tokens_list)

    for i in tokens_list:
        if i == '(':
            current_tree.insert_left('')
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()

        elif i in ['and', 'or', 'not']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()

        elif i == ')':
            current_tree = stack.pop()

        elif i not in ['and', 'or', 'not', ')']:
            try:
                if i != 'False':
                    current_tree.set_root_val(True)
                    parent = stack.pop()
                    current_tree = parent
                else:
                    current_tree.set_root_val(False)
                    parent = stack.pop()
                    current_tree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return tree


def evaluate(parse_tree):
    operates = {'and': operator.and_, 'or': operator.or_, 'not': operator.not_}

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = operates[parse_tree.get_root_val()]
        if fn == operator.and_ or fn == operator.or_:
            return fn(evaluate(left_c), evaluate(right_c))
    elif right_c:
        fn = operates[parse_tree.get_root_val()]
        if fn == operator.not_:
            return fn(evaluate(right_c))
    else:
        return parse_tree.get_root_val()


def print_exp(tree: BinaryTree) -> str:
    s_val = ""
    if tree:
        s_val = '(' + print_exp(tree.get_left_child())
        s_val = s_val + str(tree.get_root_val())
        s_val = s_val + print_exp(tree.get_right_child()) + ')'
    return s_val


if __name__ == "__main__":
    pt: BinaryTree = build_parse_tree("( ( True and False ) or False )")
    pt2: BinaryTree = build_parse_tree("not( ( True and False ) or False )")
    print(evaluate(pt))
    print(evaluate(pt2))
    print()
    pt.pre_order()
    print()
    pt.post_order()
    print()
    pt.in_order()
    print("__")
    print(print_exp(pt))
