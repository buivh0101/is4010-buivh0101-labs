# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt (CPTF):**
> Context: I am working on a Python lab. This function should return the sum of all even numbers in a list, but it is returning the wrong result.
> Persona: You are a senior Python developer and code reviewer.
> Task: Identify the bug, fix it, and explain the mistake.
> Format: Give (1) 2 bullet points explaining the bug and fix, then (2) the corrected function in one Python code block.
>
> Buggy code:
> ```python
> def sum_of_evens(numbers):
>     """Calculate the sum of all even numbers in a list.
>
>     Parameters
>     ----------
>     numbers : list of int
>         A list of integers.
>
>     Returns
>     -------
>     int
>         The sum of all even numbers in the list.
>     """
>     total = 0
>     for num in numbers:
>         if num % 2 == 1:  # This line has a bug!
>             total += num
>     return total
> ```



**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

## Problem 2: Refactoring

**My Prompt (CPTF):**
> Context: I am working on a Python lab. This function works correctly, but it is hard to read because it uses indexing and range-based loops.  
> Persona: You are a senior Python developer who focuses on writing clean, readable, and Pythonic code.  
> Task: Refactor this function to make it more concise and idiomatic while keeping the same behavior.  
> Format: Give (1) 2–3 bullet points explaining the improvements, then (2) the refactored function in one Python code block.  
>
> Code:
> ```python
> def get_names_of_adults(users):
>     """Given a list of user dictionaries, returns a list of names of users
>     who are 18 or older.
>
>     Parameters
>     ----------
>     users : list of dict
>         List of user dictionaries with 'name' and 'age' keys.
>
>     Returns
>     -------
>     list of str
>         Names of users who are 18 or older.
>     """
>     results = []
>     for i in range(len(users)):
>         if users[i]['age'] >= 18:
>             results.append(users[i]['name'])
>     return results
> ```

**AI's Refactored Code:**
```python
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    return [user["name"] for user in users if user["age"] >= 18]


---

## Problem 3: Documenting

**My Prompt (CPTF):**
> Context: I am working on a Python lab. This function calculates the area of a rectangle and raises a ValueError for invalid inputs, but it has no documentation.  
> Persona: You are a Python developer who writes professional NumPy-style docstrings.  
> Task: Write a complete NumPy-style docstring for this function, including Parameters, Returns, Raises, and Examples.  
> Format: Return only the full function with the new docstring in one Python code block.  
>
> Code:
> ```python
> def calculate_area(length, width):
>     if length <= 0 or width <= 0:
>         raise ValueError("Length and width must be positive numbers.")
>     return length * width
> ```

**AI's Documented Code:**
```python
def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Parameters
    ----------
    length : float or int
        The length of the rectangle. Must be positive.
    width : float or int
        The width of the rectangle. Must be positive.

    Returns
    -------
    float or int
        The area of the rectangle (length * width).

    Raises
    ------
    ValueError
        If length <= 0 or width <= 0.

    Examples
    --------
    >>> calculate_area(5, 3)
    15
    >>> calculate_area(2.5, 4)
    10.0
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
