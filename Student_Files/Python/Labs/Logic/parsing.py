nbrS1 = "12|23|72|238|515|7|23|723|2|5|73|567|7|33|6|14"
nbrS2 = "72|28|spam|82|75|72|3|abc|27|25|2|7|71|def|6|14"

s1_numbers = nbrS1.split("|")
s2_numbers = nbrS2.split("|")


def compute_total(string_of_numbers):
    total = 0

    numbers = string_of_numbers.split("|")

    for nbr in numbers:
        if nbr.isdigit():
            total = total + int(nbr)

    return total


s1_total = compute_total(nbrS1)

s2_total = compute_total(nbrS2)

print(f"s1_total: {s1_total}")

print(f"s2_total: {s2_total}")
