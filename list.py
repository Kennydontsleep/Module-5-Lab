for Listnum in range(50):
    if Listnum % 3 == 0 and Listnum % 5 == 0:
        print("Divisible by both")
        continue
    elif Listnum % 3 == 0:
        print("Divisible by three")
        continue
    elif Listnum % 5 == 0:
        continue
        print("Divisible by five")