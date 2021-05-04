def __private_func():
    return 'this is the test'

# This func is run private func also for private func interface.
def public_func():
    return __private_func()
