# file = open("rhyme.txt", "r")

# all_lines = file.readlines()

# print(all_lines)

# while True:
#     line = file.readline()
#     if not line:
#         break
#     else:
#         print(line)

# file.close()

# caution with this -- opening a large file might chew up memory -- could be good to read line by line instead
# with open("rhyme.txt", "r") as file:
#     data = file.read()
#     print(data)

# lines = ["One\n", "Two\n", "Three\n"]

# with open("new.txt", "a+") as file:
#     file.write(f"=" * 10 + "My Log" + "=" * 10 + "\n")
#     file.writelines(lines)
#     file.write("=" * 26 + "\n\n")

# import os

# cwd = os.getcwd()

# print(f"cwd: {cwd}")
