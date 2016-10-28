
from data_loader import get_data

from data_compiler import compile_data


def fit_data(compiled_data_dict):
    print "Fitting " + str(compiled_data_dict)


if __name__ == "__main__":
    stopping_voltages, photocurrents = get_data()
    compiled_data = compile_data(stopping_voltages, photocurrents)
    fit_data(compiled_data)
