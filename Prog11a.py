#Create a program to Join Tuples if similar initial element

def join_tuples(lst):
    result = []
    current = None

    lst.sort(key=lambda x: x[0])
    
    for tpl in lst:
        if current is None:
            current = tpl
        elif current[0] == tpl[0]:
            current = tuple(set(current + tpl))
        else:
            result.append(current)
            current = tpl

    if current is not None:
        result.append(current)
    
    return result

tuples_list = []
while True:
    tpl_str = input("Enter tuple of two numbers (separated by space) (e.g., '9 8'). \nPress Enter to stop: ")
    if not tpl_str:
        break
    tpl_data = tuple(map(int, tpl_str.split()))
    tuples_list.append(tpl_data)

modified_list = join_tuples(tuples_list)

print("Answer:", modified_list)