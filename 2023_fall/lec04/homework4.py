
def list_to_dict(input_list):
    """
    This function should return a dictionary in which each element of 
    `input_list` is a value, and the corresponding key is the numerical 
    index of that element in `input_list`.
    """
    result_dict = {} 
    for index, value in enumerate(input_list):
        result_dict[index] = value  
    return result_dict


example_list1 = [1, 3.14, "hello", True]
example_list2 = ["a", "a", "a"]
example_list3 = []

result1 = list_to_dict(example_list1)
result2 = list_to_dict(example_list2)
result3 = list_to_dict(example_list3)

print(result1) 
print(result2)  
print(result3) 



