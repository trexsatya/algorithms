from queue import LifoQueue


def matching_bracket(c):
    if c == ')':
        return '('
    if c == '}':
        return '{'
    if c == ']':
        return '['


def is_balanced(exp: str):
    stack = LifoQueue(maxsize=len(exp))
    for c in exp:
        # If left brackets
        if c in ['(', '{', '[']:
            stack.put(c)
        else:
            on_top = None if stack.qsize() == 0 else stack.get()
            if on_top != matching_bracket(c):
                return False

    return stack.qsize() == 0


print(is_balanced("{"))
