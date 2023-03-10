# open_russion_doll()

The script demonstrates the concept of recursion, which is a way of solving a problem by having a function call itself and perform the same operation multiple times with different inputs, while trying smaller inputs in every step to make the problem smaller. A base condition is necessary to stop the recursion, otherwise an infinite loop will occur.

The `open_russian_doll` function takes an integer parameter doll, which represents the number of dolls to open.
The function starts with a base condition that checks if `doll` is equal to 1, in which case it prints `"Last doll opened"` and stops the recursion.
If `doll` is greater than 1, the function prints `"Open doll number"` followed by the current value of doll, and then calls itself with the parameter `doll = doll-1`.
This process continues until the base condition is met and the recursion stops.



The script includes a docstring that explains the concept of recursion and how to use the `open_russian_doll` function.
The if `__name__ == "__main__":` block at the end of the script calls the `open_russian_doll` function with an argument of 5 to demonstrate the functionality of the script.
