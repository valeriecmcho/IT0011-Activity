# Define the sets
A = {'a', 'b', 'd', 'f', 'g'}
B = {'b', 'c', 'd', 'f', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

# Part (a): Elements in both A and B
intersection_A_B = A & B
print("a. Number of elements in A and B:", len(intersection_A_B))

# Part (b): Elements in B that are not in A and C
B_not_in_A_C = B - (A | C)
print("b. Number of elements in B that are not in A and C:", len(B_not_in_A_C))

# Part (c): Showing specific sets using set operations

# i. Elements in C that are unique
unique_C = C - (A | B)
print("c.i:", unique_C)

# ii. Elements in both B and C
B_and_C = B & C
print("c.ii:", B_and_C)

# iii. Elements in A, B, or C but not all three
union_ABC = A | B | C
intersection_ABC = A & B & C
not_all_three = union_ABC - intersection_ABC
print("c.iii:", not_all_three)

# iv. Elements in A and B but not C
A_B_not_C = (A & B) - C
print("c.iv:", A_B_not_C)

# v. Elements in B but not in A or C
B_not_A_C = B - (A | C)
print("c.v:", B_not_A_C)

# vi. Elements unique to B
unique_B = B - (A | C)
print("c.vi:", unique_B)
