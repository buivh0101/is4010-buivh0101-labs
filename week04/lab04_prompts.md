# Lab 04 Prompts

## Problem 1
My prompt: “I have two very large Python lists of product IDs. I need to find which IDs appear in both lists. The order of the result does not matter, but performance is important. What Python data structure should I use and why?”

AI recommendation: Set

Reasoning: 
    Convert both lists to sets.
    Use set intersection to find common elements.
    Sets remove duplicates automatically.
    Set operations run much faster than looping through lists.

## Problem 2
My prompt:“I have a list of user profiles, where each user is a dictionary with keys ‘name’, ‘age’, and ‘email’. I need to look up a user by name very frequently. Performance is critical. What data structure should I use and why?”

AI recommendation: Dictionary

Reasoning:
    Convert the list of users into a dictionary with name as the key.
    This allows O(1) lookup time instead of scanning the whole list.
    Dictionaries are built for fast key-based access.
    This is far more efficient than searching a list every time.

## Problem 3
My prompt:“I have a list of integers. I need to return only the even numbers, but I must keep them in the exact same order they appeared. What data structure and approach should I use and why?”

AI recommendation: List with list comprehension

Reasoning:
    A list preserves order automatically.
    List comprehension is a clean and fast way to filter values.
    Checking n % 2 == 0 correctly identifies even numbers, including zero and negatives.
    This keeps the original sequence while removing odd numbers.
