def find_common_elements(list1, list2):
    """Find the common elements between two lists."""
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 & set2)


def find_user_by_name(users, name):
    """Find a user's profile by name from a list of user data."""
    user_dict = {user["name"]: user for user in users}
    return user_dict.get(name, None)


def get_list_of_even_numbers(numbers):
    """Return a new list containing only the even numbers from the input list."""
    return [n for n in numbers if n % 2 == 0]
