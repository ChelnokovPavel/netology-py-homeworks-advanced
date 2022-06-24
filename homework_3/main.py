class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.data = []

    def flatten(self, lst):
        for el in lst:
            if isinstance(el, list):
                self.flatten(el)
            else:
                self.data.append(el)

    def __iter__(self):
        self.flatten(self.nested_list)
        return self

    def __next__(self):
        try:
            return self.data.pop(0)
        except IndexError:
            raise StopIteration


def flat_generator(nested_list):
    if isinstance(nested_list, list):
        for i in nested_list:
            for j in flat_generator(i):
                yield j
    else:
        yield nested_list


if __name__ == '__main__':
    print('Задачка 1, 3')
    nested_list = [
        ['a', ['b', ['z', True]], 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('\nЗадачка 2, 4')
    for item in flat_generator(nested_list):
        print(item)
