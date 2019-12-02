# Solutions/Collections/parsing.py
#

inStr = "12|23|72|238|55|7|23|12|2|23|73|56|23|33|6|7"
print(inStr)
nbrs_s = inStr.split("|")
nbrs = []
for s in nbrs_s:
    nbrs.append(int(s))
print("before filter:")
print( nbrs )
nbrs = set( nbrs )
nbrs = list( nbrs )
print("after filter:")
print( nbrs )