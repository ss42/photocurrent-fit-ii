
import csv

STOPPING_VOLTAGE_FILE_PATH = "data/TEK0000.CSV"

PHOTOCURRENT_FILE_PATH = "data/TEK0001.CSV"

# The oscilloscope data files each have 18 lines of informational output before the actual data begins.
HEADER_LINES_TO_DISCARD = 18

# The column of interest in both of the oscilloscope data files is the fifth column (one-based).
COLUMN_OF_INTEREST = 4  # 0-based


def read_oscilloscope_data(data_file_path, max_lines=0):
    headers_left_to_discard = HEADER_LINES_TO_DISCARD
    lines_read = 0
    data = []

    with open(data_file_path, 'rb') as data_file:
        oscilloscope_data_reader = csv.reader(data_file, delimiter=',')
        for row in oscilloscope_data_reader:
            if headers_left_to_discard > 0:
                headers_left_to_discard -= 1
            else:
                lines_read += 1
                if max_lines != 0 and lines_read > max_lines:
                    # max_lines has been reached, return early
                    return data
                else:
                    datum = row[COLUMN_OF_INTEREST]
                    datum_as_float = float(datum)
                    data.append(datum_as_float)

    return data


def read_stopping_voltages(**kwargs):
    return read_oscilloscope_data(STOPPING_VOLTAGE_FILE_PATH, **kwargs)


def read_photocurrents(**kwargs):
    return read_oscilloscope_data(PHOTOCURRENT_FILE_PATH, **kwargs)


def get_data():
    stopping_voltages = read_stopping_voltages()
    photocurrents = read_photocurrents()

    count = len(stopping_voltages)

    # Something is wrong with our data if the number of stopping voltage values
    # differs from the number of photocurrent values.
    other_count = len(photocurrents)
    if count != other_count:
        print "Exiting! Stopping voltages count was {0} but photocurrents count was {1}.".format(str(count),
                                                                                                 str(other_count))
        exit(-1)

    return stopping_voltages, photocurrents
