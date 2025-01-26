from eccodes import *


INPUT = "data/data.grib"

with open(INPUT, 'rb') as f:
    gid = codes_grib_new_from_file(f)

    values = codes_get_values(gid)
    print(values)
    exit()
    num_vals = len(values)
    for i in range(num_vals):
        print("%d %.10e" % (i + 1, values[i]))

    print('%d values found in %s' % (num_vals, INPUT))

    for key in ('max', 'min', 'average'):
        print('%s=%.10e' % (key, codes_get(gid, key)))

    # Example of accessing specific elements from data values
    # Get first, middle and last elements
    indexes = [0, int(num_vals/2), num_vals-1]
    elems = codes_get_double_elements(gid, 'values', indexes)

    codes_release(gid)
