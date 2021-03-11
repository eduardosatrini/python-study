# Using decorator to measure time

import time

def time_measure(func): # func = function
    time_0 = time.time()
    func()
    time_1 = time.time() # duration
    return time_1 - time_0


@time_measure # decorator
def slow_code():
    time.sleep(2)

print(slow_code)
