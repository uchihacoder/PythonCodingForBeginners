# Solutions/Logic/parsing.py
#

nbrS1 = "12|23|72|238|515|7|23|723|2|5|73|567|7|33|6|14"
nbrS2 = "72|28|spam|82|75|72|3|abc|27|25|2|7|71|def|6|14"
nbrL1 = nbrS1.split("|")
print("len={}".format(len(nbrL1)))
print(nbrL1)

print("sum calculated with for loop:")
sum = 0
for s in nbrL1:
    sum += int(s)
print("sum={}".format(sum))
print("-"*50)

nbrL2 = nbrS2.split("|")
print("len={}".format(len(nbrL2)))
print(nbrL2)

print("sum calculated with for loop:")
sum = 0
for s in nbrL2:
    if(s.isdigit()):
        sum += int(s)
print("sum={}".format(sum))

print("sum calculated with while loop:")
sum = 0
i = 0
while i < len(nbrL2):
    s = nbrL2[i]
    if(s.isdigit()):
        sum += int(s)
    i += 1
print("sum={}".format(sum))