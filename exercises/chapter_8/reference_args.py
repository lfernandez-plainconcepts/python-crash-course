def modify_argument(string_arg):
    """Modify the argument by appending a string."""
    string_arg += " modified"
    print(f"Inside function: {string_arg}")
    return string_arg

arg_01 = "original"
print(f"Before function call: {arg_01}")
arg_modified = modify_argument(arg_01)
print(f"After function call: {arg_01}")
print(f"Modified argument: {arg_modified}")

def modify_argument_number(number_arg):
    """Modify the argument by adding 1."""
    number_arg += 1
    print(f"Inside function: {number_arg}")
    return number_arg

number_arg_01 = 1
print(f"Before function call: {number_arg_01}")
number_arg_modified = modify_argument_number(number_arg_01)
print(f"After function call: {number_arg_01}")
print(f"Modified argument: {number_arg_modified}")


def modify_list(list_arg):
    """Modify the argument by appending an item to the list."""
    list_arg.append("new item")
    print(f"Inside function: {list_arg}")
    return list_arg

list_01 = ["item1", "item2"]
print(f"Before function call: {list_01}")
list_modified = modify_list(list_01)
print(f"After function call: {list_01}")
print(f"Modified list: {list_modified}")

