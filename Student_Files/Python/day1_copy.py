import copy


def print_info(stuff):
    print(id(stuff), stuff)


shallow_list = [12, 23, 48, 2]
deep_list = [[12, 23], [48, 2]]

# shallow copy -- only typically useful when dealing with primatives
shallow_copy = copy.copy(shallow_list)

# deep copy -- most often this is what we want -- knows how to copy memory locations
deep_copy = copy.deepcopy(deep_list)

shallow_list[2] = 17

deep_list[0] = [1, 2]

print_info(shallow_list)

print_info(shallow_copy)

print_info(deep_list)

print_info(deep_copy)
