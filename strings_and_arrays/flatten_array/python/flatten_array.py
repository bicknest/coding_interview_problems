import functools


def reducer(flat, to_flatten):
    if isinstance(to_flatten, list):
        return flat + flatten_array(to_flatten)
    else:
        return flat + [to_flatten]

def flatten_array(array):

    return functools.reduce(reducer, array, [])
