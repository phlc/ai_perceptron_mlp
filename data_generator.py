
def __set_generator_rec(size, set, list = [], level = 0):
    if(level >= size):
        set.append(list)

    else:
        __set_generator_rec(size, set, list + [0], level+1)
        __set_generator_rec(size, set, list + [1], level+1)

def __set_generator(size = 2):
    set = []
    __set_generator_rec(size, set)
    return set


def __labels_generator(operator, set = []):
    labels = []
    for inputs in set:
        if (operator == 'AND'):
            labels.append(0 if 0 in inputs else 1)

        elif (operator == 'OR'):
            labels.append(1 if 1 in inputs else 0)

        elif (operator == 'XOR'):
            labels.append(0 if inputs.count(1)%2==0 else 1)
    
    return labels

def generator(operator, size = 2):
    operators = ['AND', 'OR', 'XOR']
    operator = operator.upper()
    if(size < 2):
        raise ValueError("Size must be greater than 2")
    if(operator not in operators):
        raise NameError("Operators are 'AND', 'OR', 'XOR'")
    

    set = __set_generator(size)
    labels = __labels_generator(operator, set)
    return (set, labels)