def build_person(first_name, last_name, age=None):
    """Build a dictionary containing information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age # Optional age parameter    
    
    return person

musician = build_person("jimi", "hendrix", age=27)
print(musician)