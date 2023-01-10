import time

def long_calculation():
    for i in range(1,10000):
        i=i+1
        v=i%2
        c=i+v
    return c

def  waiting_function():
    start_time = time.time()
    time.sleep(20)
    return "The time required to extract information: " + str(time.time() - start_time) + " seconds"