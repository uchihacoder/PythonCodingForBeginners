import re

# =====MATCH=====

# telephone_number = "206-555-1212"

# # # ^ indicates the start of the line, $ the end of the line and the + indicates more than 1 numbers
# match = re.search("^[0-9]{3}-[0-9]{3}-[0-9]{4}$", telephone_number)

# if match:
#     print(f"valid telephone number")
# else:
#     print("invalid telephone number")

postal_code = "98166-1234"

# match = re.search("^[0-9]{5}(-[0-9]{4})?$", postal_code)

# if match:
#     print(f"valid postal code")
# else:
#     print("invalid postal code")

# =====FINDALL=====

# results = re.findall("[0-9]+", postal_code)

# print(results)

# for result in results:
#     print(result)

# =====SUBSTITUTE=====

phrase = "I am a little teapot"

updated_phrase = re.sub("am", "AM", phrase)

print(updated_phrase)
