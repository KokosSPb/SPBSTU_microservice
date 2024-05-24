import time

def get_exec_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Execution time: " + str(end_time - start_time))
        return result
    return wrapper
	
@get_exec_time
def add(a, b):
    print(a+b)
	
@get_exec_time
def add_from_file():
    with open("input.txt", "r") as input_file:
        a, b = map(int, input_file.readlines())

    result = a + b

    with open("output.txt", "w") as output_file:
        output_file.write(str(result))
		
add(3, 9)
add_from_file()