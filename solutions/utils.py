import os


def datapath(filename):
    solutions_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(os.path.dirname(solutions_dir), 'data', filename)
    return data_dir
