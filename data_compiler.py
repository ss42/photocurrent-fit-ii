

# remove the following comment line after implementing
# it is just there to temporarily suppress a warning in the unimplemented function

def compile_data(stopping_voltages, photocurrents):

    # We have two data arrays. The photocurrents are the independent (y) values. The stopping voltages
    # are the dependent (x) values.

    # These need to be compiled into a single dictionary whose keys are the x values and whose values are
    # tuples containing the sum of y values, the sum of the squares of the y values, and their count.

    compiled_data = dict()

    idx = 0
    for stopping_voltage in stopping_voltages:
        photocurrent = photocurrents[idx]
        if stopping_voltage in compiled_data:
            a_sum, sum_of_squares, count = compiled_data[stopping_voltage]
            a_sum += photocurrent
            sum_of_squares += photocurrent * photocurrent
            count += 1
            compiled_data[stopping_voltage] = a_sum, sum_of_squares, count
        else:
            compiled_data[stopping_voltage] = photocurrent, photocurrent * photocurrent, 1
        idx += 1

    return compiled_data
