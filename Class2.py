"""Class 2 about functions in python"""

def is_even(number):
    """ check if the number is even

    :param      number      A number to check 
    :return     wheather or not the vaule is even
    """
    if number % 2 == 0:
        return True
    else:
        return False
    
    

    
def print_odds(items):
    """Print the only odd numbers from the given list 

    :param      items       list of numbers
    :return     nothing     
    """
    for item in items:  #loop each item in the list
        #here, item will equal each thing in the list, one by one 
        check_even = is_even(item)

        if not check_even:
            print(item)




def find_greatest_value(items):
    """Find and return the greatest vaule in given list

    example: [10, 2, 3, 7,] shoudl return 10
    """

    """ Not using the too MAX
    max_number = items[0]
    for item in items[1:]:

        if item > max_number:
            max_number = item
    print(max_number)
    """

    max_number = max(items)
    print(max_number)       



def get_every_other_element(items):

    """Return a list of contaoning the evn-indexed items in the given list
    example: given [2, 6, 2, 5], this returns [2, 2]
       here, the 2s are idex: [0] and [2]
    """

    index_number = items[0]

    for item in items[0:]:
        check_index = is_even(item)

        if not check_index:
            print(item)
        

