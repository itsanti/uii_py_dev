def get_data(path):
    with open(path, 'r', encoding='utf=8') as f:
        # skip first line
        keys = f.readline()[:-1].split(',')
        result = [dict(zip(keys, line[:-1].split(','))) for line in f]
    return result