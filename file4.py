def greet(**kwargs):
    return f"Hello from {kwargs.get('name')} {kwargs.get('family_name')}!"


print(greet(name="Moslem", family_name="Amiri"))
