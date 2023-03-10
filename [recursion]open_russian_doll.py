# open_russian_doll.py

# Author: Alin Morosanu
# Date: 10/03/2023

# Description: 
#   RECURSION is a way of solving a problem by having a function calling itself and:
#     - performing the same operation multiple times with different inputs
#     - in every step we try smaller inputs to make the probme smaller.
#     - Base condition is needed to stop the recursion, otherwise infinite loop will occur



def open_russian_doll(doll: int) -> None:
    """
    Description: 
    RECURSION is a way of solving a problem by having a function calling itself and:
        - performing the same operation multiple times with different inputs
        - in every step we try smaller inputs to make the probme smaller.
        - Base condition is needed to stop the recursion, otherwise infinite loop will occur
    
    How to use:
    Call the function with the number of dolls you want to open
    
    open_russian_doll(5)
    """
    # Base condition
    if doll == 1:
        print("Last doll opened")
    # Recursive condition
    else: 
        print("Open doll number", doll)
        open_russian_doll(doll-1)

if __name__ == "__main__":
    open_russian_doll(5)


