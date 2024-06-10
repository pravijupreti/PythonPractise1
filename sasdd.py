while True:
    try:
        var1 = int(input("Give a number: "))
        if isinstance(var1, int):
            break
    except Exception:
        print("This input is invalid.")


while True:
    try:
        var2 = int(input("Give a number: "))
        if isinstance(var2, int):
            break
    except Exception:
        print("This input is invalid.")