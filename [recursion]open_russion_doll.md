# Recursion Algorithm

### open_russion_doll()

The script demonstrates the concept of recursion, which is a way of solving a problem by having a function call itself and perform the same operation multiple times with different inputs, while trying smaller inputs in every step to make the problem smaller. A base condition is necessary to stop the recursion, otherwise an infinite loop will occur.

The `open_russian_doll` function takes an integer parameter doll, which represents the number of dolls to open.
The function starts with a base condition that checks if `doll` is equal to 1, in which case it prints `"Last doll opened"` and stops the recursion.
If `doll` is greater than 1, the function prints `"Open doll number"` followed by the current value of doll, and then calls itself with the parameter `doll = doll-1`.
This process continues until the base condition is met and the recursion stops.

The script uses Python's type hints, which provide a way to annotate function arguments and return values with their expected data types. In this case, the `open_russian_doll` function takes an integer parameter doll and returns None, as specified in the type hints for the function:

The : int after the doll parameter indicates that it is expected to be an integer, and the -> None after the function definition indicates that the function returns None.

Using type hints can help improve code readability, maintainability, and can also help catch type-related bugs during development.

The script includes a docstring that explains the concept of recursion and how to use the `open_russian_doll` function.
The if `__name__ == "__main__":` block at the end of the script calls the `open_russian_doll` function with an argument of 5 to demonstrate the functionality of the script.

### When to use recursion?

When the problem can be devided into similar sub-problems. The sub-problem must be similar, otherwise recursion it's not a choice.

### How can we know if the sub-problem it's similar?

Usually when the problem begins with the following statements:
- design an algorithm to compute nth ...
- write code to list the n ...
- implement a methos to compute all.
- in general, when the input isn't huge, and the memory can handle it.

### When NOT to use recursion?
- when time and space complexity materrs for us.
