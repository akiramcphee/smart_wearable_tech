from fabrication import generate_random_variation


class Fabrication(object):
    def __init__(self, filename, var_num):
        self.filename = filename
        self.var_num = var_num

    def generate_random_variation(self, kind):
        self.kind = kind
        generate_random_variation(self.filename, self.var_num, self.kind)
        pass


if __name__ == '__main__':
    i = 0
    while i < 11:  # Loop through the different scopes
        j = 0
        while j < 100:  # Number of samples for each scope
            filename = f'fabricated_data/csv/scope_{i}.csv'
            scope = Fabrication(filename, j)
            scope.generate_random_variation(kind='image')
            j += 1
        i += 1
