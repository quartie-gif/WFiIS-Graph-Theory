class DistanceMatrix:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for x in range(size)] for y in range(size)]

    def __str__(self):
        return_string = ''
        for i in range(self.size):
            for j in range(self.size):
                return_string += str(self.matrix[i][j]) + '\t'
            return_string += '\n'
        return return_string

    def __iter__(self):
        return self.__next__()

    def __next__(self):
        for i in range(self.size):
            for j in range(self.size):
                yield self.matrix[i][j]

    def __getitem__(self, key):
        return self.matrix[key]

    def set(self, x, y, value):
        self.matrix[x][y] = value

    def get(self, x, y):
        return self.matrix[x][y]

    def insert(self, x, y, value):
        self.matrix[x][y] = value
        self.matrix[y][x] = value
