import json
"""
person = {
    "name": "John",
    "age": 30,
    "city": "Nework",
    "hometown": "sindhuwa",
    "title": ["Engineer", "Programmer"]

}
print("________________________________________________________________________")

#now ecoding json data
personJSON = json.dumps(person, indent=4, sort_keys=4, separators= ('; ', '= '))
print(person)
print("\n")

print(personJSON)
personJSON = json.dumps(person, indent=4, sort_keys=4)

with open('person.json', 'w') as file:
    json.dump(person, file, indent = 4)
 

person = json.load(personJSON)

print(person)

print("________________________________________________________________________")

#Decoding json data

personJSON = json.dumps(person, indent=4, sort_keys= True)


with open('person.json', 'r') as file:
    person = json.load(file)

    print(person)



"""
print("________________________________________________________________________")
class User:
    def __init__(self,name, age):
        self.name = name
        self.age = age

user = User('sajan', 27)

def encode_user(o):
    if isinstance(o,User):
        return {'name':o.name, 'age': o.age, o.__class__.__name__:True}
    else:
        raise TypeError ('Object of the json is not json serializable')

userJSON = json.dumps(user, default= encode_user)
print(userJSON)

print("________________________________________________________________________")

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return{'name':o.name, 'age':o.age, o.__class__.__name__:True}
        return JSONEncoder.default(self,o)
#userJSON = json.dump(user, cls = UserEncoder)

userJSON = UserEncoder().encode(user)

print(userJSON)

print("________________________________________________________________________")

#decode object back

print("________________________________________________________________________")
user = json.loads(userJSON)
print(user)
print(type(user))

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct(['name'], age = dct['age']))
user = json.load(userJSON, object_hook = decode_user)

print(type(user))
print(user.name)


