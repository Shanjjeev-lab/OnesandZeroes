def findZeroesAndOnes(num):
    ones = 0
    zeroes = 0

    while num > 0:
        if num & 1 == 1:
            ones+= 1
        else:
            zeroes += 1
        num = num >> 1
    print("Ones: ", ones)
    print("Zeroes:", zeroes)

num = 69
print(f"Bin of {num}: {bin(num)[2:]}")
findZeroesAndOnes(num)