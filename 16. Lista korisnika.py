import random
people = []

for x in range(0,8):
    person = input("Unesite ime osobe: ")
    people.append(person)

index = random.randint(0,7)

random_person = people[index]

print("Biranje nasumične osobe je:", random_person)
