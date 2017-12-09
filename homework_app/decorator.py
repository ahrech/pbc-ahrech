def print_args(fn):
    def wrapped(*args):
        print "{}{}".format(fn.__name__, args)
        return fn(*args)
    return wrapped
