# Solutions/Logic/looping.py
#

cnt = 0
for i in range(10):
    for j in range(10):
        cnt += 1
        if ((cnt % 5)==0):
            continue
        print("{:>4}".format(cnt), end=' ')
    print()