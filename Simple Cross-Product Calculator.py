# Simple Cross-Product Calculator
# Poorly-formatted (but it works) by ricky8k

print("Simple Cross-Product Calculator")
print("\n| i | j | k | i | j |\n| _ | \ | \ | \ | _ |\n| _ | _ | \ | \ | \ |")
print("____________________\n")

# Input vectors for A
print("Enter vector A:")
i1 = int(float(input("")))
j1 = int(float(input("")))
k1 = int(float(input("")))
# Input vectors for B
print("Enter vector B:")
i2 = int(float(input("")))
j2 = int(float(input("")))
k2 = int(float(input("")))

print("\n____________________")
# Final input for user to double-check
print("Input:")
print(str(float(i1)) + "i " + str(float(j1)) + "j " + str(float(k1)) + "k ")
print(str(float(i2)) + "i " + str(float(j2)) + "j " + str(float(k2)) + "k ")

# Solution calculated by using table:
#   | i | j | k | i | j |
# 1 | _ | b | _ | _ | _ | 
# 2 | _ | _ | b | _ | _ |
# e.g. (j1 * k2) = (b * b)
print("\nSolution:")
print(str(float(j1 * k2)) + "i " + str(float(k1 * i2)) + "j " + str(float(i1 * j2)) + "k")
# "i" and "j" swapped places in line 2 to make addition easier
# Multiply all variables by (-) in line below
print(str(float(-(k1 * j2))) + "i " + str(float(-(i1 * k2))) + "j " + str(float(-(j1 * i2))) + "k")
print("--------------------")
# Add both halves to get final answer:
print(str(float((j1 * k2) + (-(k1 * j2)))) + "i " + str(float((k1 * i2) + (-(i1 * k2)))) + "j " + str(float((i1 * j2) + (-(j1 * i2)))) + "k")

print("\nhttps://github.com/ricky8k")
# Made by ricky8k
# https://github.com/ricky8k
