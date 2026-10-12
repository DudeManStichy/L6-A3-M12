input("Bit difference - XOR shows which bits are different. Press enter to continue...")
print(" 5 ^ 3 =" , 5 ^ 3, "binary", bin(5 ^ 3)[2:], " bits different:", bin(5 ^ 3).count('1'))
print(" 9 ^ 5 =", 9 ^ 5, "binary", bin(9 ^ 5)[2:], " bits different:", bin(9 ^ 5).count('1'))

n = int(input("Enter a number (try 4 or 6): "))
guess = input("How many bits are different between " + str(n) + " and 7? ")
input("XOR marks the different bits - count the 1's. Press Enter to continue...")
diff = bin(n ^ 7).count('1')
print(" ", n, "^ 7 =", n ^ 7, "binary", bin(n ^ 7)[2:], " bits different:", diff, "your guess:", guess)