for nbr in range(1, 100):
    if not nbr % 5 == 0 and not nbr % 10 == 0:
        print(nbr, end="  ")
    elif nbr % 10 == 0:
        print("\n")
