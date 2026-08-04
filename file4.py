def greet(**kwargs):
    return f"Hello {kwargs.get('name')}!"


print(greet(name="Moslem"))
