# Set - collection of unique objects
averyuselesslist=[1,2,3,2,1,4,5,4,3,5]
print(averyuselesslist)
print(type(averyuselesslist))
set1=set(averyuselesslist)
print(set1)
print(type(set1))

if 6 in set1:
    print("6 is not in set1")
else:
    print("6 is not in set1")

mySet = set([])
mySet.add(100)
mySet.add(66)
mySet.add(67)
mySet.add(68)
mySet.add(69)
print(mySet)

mySet.remove(100)
print(mySet)

# remove will throw error if the element is not present in the set
# mySet.remove(50)

# Discard will not show an error, evenif the number does not exist in the set
mySet.discard(40)

# Set operations
# 1) Union
# 2) Intersection
# 3) Difference
# 4) Symmetric Difference

a = {1,2,3,4,5}
b = {4,5,6,7,8}

print("Set a : ", a)
print("Set a : ", b)

# Union means addition of sets
print("Union of two sets")
print(a.union(b))
print(a | b)

# Intersection prints the common element between the two sets
print("Intersection of two sets")
print(a.intersection(b))
print(a & b)

# Difference of A and B is the elements that exist in A but not in B

print("difference of two sets")
print(a.difference(b))
print(a - b)
print(b.difference(a))
print(b - a)

# Symmetric Difference removes the common element from a and b
print("Symmetric difference of a and b")
print(a.symmetric_difference(b))
print(a ^ b)
