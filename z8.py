person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

#a
for k in person:
    print(f"{k} -> {person[k]}")

#b
print(f"Name: {person['name']}")

#c
print(f"Hobbies: {person['hobby'][0]} and {person['hobby'][1]}")

#d
person['surname'] = "Nowak"
print(f"New surname is: {person['surname']}")

#e
person['married'] = False
print(f"Marrige status: {person['married']}")

#f
person['gender'] = "male"
print(f"Gender: {person['gender']}")

#g
person['hobby'].append("running")
print(f"Hobbies: {person['hobby']}")

#h
person['phone']['workphone'] = "313131444"
print(f"Phone numbers: {person['phone']}")
