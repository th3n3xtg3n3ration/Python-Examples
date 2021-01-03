def add(param1, param2):
    if -1000 <= param1 <= 1000:
        if -1000 <= param2 <= 1000:
            return param1 + param2
    else:
        print("Please fit the constraints.")
        print("Ex. -1000 ≤ param1 ≤ 1000.")


add(3000, 1000)