def get_file(filename):
    with open(filename, 'r') as in_file:
        lines = in_file.readlines()
        return '\n'.join(lines)