# Part II
# This script asks for a person's ID and shows that person's info and pets.

import sqlite3

# connect to the database
conn = sqlite3.connect("pets.db")
cursor = conn.cursor()

while True:
    user_input = input("Enter a person ID number (-1 to quit): ")

    # stop the program if user enters -1
    if user_input == "-1":
        print("Goodbye.")
        break

    # check that input is a number
    try:
        person_id = int(user_input)
    except ValueError:
        print("Please enter a valid number.")
        continue

    # find the person
    cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
    person = cursor.fetchone()

    if person is None:
        print("Person not found.")
        continue

    first_name, last_name, age = person
    print(f"{first_name} {last_name}, {age} years old")

    # find all pets for that person
    cursor.execute("""
        SELECT pet.name, pet.breed, pet.age, pet.dead
        FROM pet
        JOIN person_pet ON pet.id = person_pet.pet_id
        WHERE person_pet.person_id = ?
    """, (person_id,))

    pets = cursor.fetchall()

    if len(pets) == 0:
        print(f"{first_name} {last_name} does not own any pets.")
    else:
        for pet in pets:
            pet_name, breed, pet_age, dead = pet

            if dead == 1:
                print(f"{first_name} {last_name} owned {pet_name}, a {breed}, that was {pet_age} years old")
            else:
                print(f"{first_name} {last_name} owns {pet_name}, a {breed}, that is {pet_age} years old")

# close the connection
conn.close()
