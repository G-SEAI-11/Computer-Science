print("---1. Create and print a dictionary")
person = {"name": "Michael", "age": 35, "city": "Hamburg"}
print(person)

print("---2. Access Dictionary Elements---")
name = person.get("name", None)
test_name = person.get("großer_zeh", None)
print(name)
print(test_name)
# print(person["name"]) # per Square Brackets zugreifen, wenn es den Key gibt
print(person.keys())
print(person.values())
print(person.items())

print("---3. Check for Key Existence---")
print("Age in person:", "age" in person)

print("---4. Change and Update Dictionary Elements---")
person["city"] = "Munich"
person.update({"age": 26, "occupation": "IT Informatiker"})
print(person)

print("---5. Add New Items to the Dictionary---")
person["country"] = "USA"
print(person)
person.update({"hobby": "cycling"})
print(person)

print("---6. Remove Items from the Dictionary---")
print(person.pop("country"))
print(person.popitem())
del person["occupation"]
print(person)
# print(person.clear())

print("---7. Copy a Dictionary---")
person_copy = person.copy()
person["age"] = 40
print("Original:", person)
print("Kopie:", person_copy)
person_constructor_copy = dict(person)
print(person_constructor_copy)

# robin = dict([("name", "robin"), ("profession", "sidekick")])
# print(robin)

print("---8. Using setdefault()---")
city = person.setdefault("city", "Berlin")
print("City:", city)
occupation = person.setdefault("occupation", "Engineer")
print("Occupation:", occupation)
print("Dictionary:", person)
