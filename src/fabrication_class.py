from fabrication import generate_random_variation


class Fabrication(object):
    def __init__(self, filename, var_num):
        self.filename = filename
        self.var_num = var_num

    def generate_random_variation(self, kind):
        self.kind = kind
        generate_random_variation(self.filename, self.var_num, self.kind)
        pass


filename = 'fabricated_data/scope_0.csv'
i = 1
while i < 10:
    scope_0 = Fabrication(filename, i)
    scope_0.generate_random_variation(kind='csv')

    i += 1
