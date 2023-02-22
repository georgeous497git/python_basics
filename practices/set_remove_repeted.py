print('Removing duplicated using set() function')

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}


def remove(params):
    new_set = set()
    for p in params:
        print(p)
        temp_set = set(p)
        new_set.update(temp_set)

    return new_set


new_set = remove([countries, northAm, centralAm, southAm])
print(f'Set = {new_set}')


new_set = countries | northAm | centralAm | southAm
print(f'Set = {new_set}')