def read_data_file(filename):
    X = []
    y = []
    with open(filename, 'r') as f:
        for line in f:
            data = map(lambda x: float(x), filter(None, line.strip().split(' ')))
            X.append(data[1:])
            y.append(data[0])
    return X, y
