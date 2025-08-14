from memory_profiler import profile

@profile
def create_list():
    my_list = [i for i in range(100000)]
    return my_list

if __name__ == "__main__":
    create_list()