friends={'tom': 7899, 'jerry': 432, 'satya': 790580}
print(friends)

#pooitem() picks elemnt form dictionary and delete it
print(friends.popitem()) #picks ('satya', 790580) randomly
print(friends) #{'tom': 7899, 'jerry': 432} after deletion

#clear() delete evrything from dictionary
print(friends.clear())
print(friends) #{}

friends={'tom': 7899, 'jerry': 432, 'satya': 790580}

#keys() returns all keys in dictionary as tuple
print(friends.keys()) #dict_keys(['tom', 'jerry', 'satya'])

#values() returns all values in dictionary as tuple
print(friends.values()) #dict_values([7899, 432, 790580])

#get(key) return value of key, returns none if no value found instaed of throwing exception KeyError
print(friends.get('satya')) #790580
print(friends.get("ankit")) #None

#pop() removes item from dictionary, if key not found it throws KeyError
print(friends.pop("tom")) #7899
print(friends) #{'jerry': 432, 'satya': 790580}
