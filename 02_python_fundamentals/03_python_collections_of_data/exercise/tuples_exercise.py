# cat, dog, cow, rabbit, dog
print("---1. Create a Tuple---")
my_tuple = ("cat", "dog", "cow", "rabbit", "dog", "cow")
print("---2. Print a Tuple---")
print(my_tuple)

print("---3. Access Tuple Items---")
print("Erstes Element:", my_tuple[0])
print("Letztes Element:", my_tuple[-1])

print("---4. Slice the Tuple---")
print(my_tuple[1:4])
print(my_tuple[:3])
print(my_tuple[2:])

print("---5. Check if an Item Exists---")
if "cat" in my_tuple:
    print("Cat is in tuple")
print("Is cat in my_tuple?", "cat" in my_tuple)


print("---6. Count and Index---")
print("Anzahl von Cow ist", my_tuple.count("cow"))
print("Erste Indexposition von Cow ist", my_tuple.index("cow"))

print("---7. Packing and Unpacking---")
tier1, tier2, tier3, tier4, tier5, tier6 = my_tuple
print(tier3)
tier1, *rest_tiere, tier6 = my_tuple
print(tier1, rest_tiere, tier6)

print("---8. Joining Tuples---")
another_tuple = ("horse", "duck")
combined_tuple = another_tuple + my_tuple
print(combined_tuple)
repeated_tuple = another_tuple * 20
print(repeated_tuple)
