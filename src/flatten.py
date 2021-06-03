
#Recursive flatten of lists for an arbitrary nested list of lists
def flatten(list_of_lists):
    #If it's empty,so the end of a list, return self
    if len(list_of_lists) == 0:
        return list_of_lists
    #If it's a list and the first element is also list, call flatten on the first element of the list and on the rest of the list
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    #If the first element is not a list, return the first element and flatten the rest
    return list_of_lists[:1] + flatten(list_of_lists[1:])

