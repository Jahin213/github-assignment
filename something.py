def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

def shout(name):
    return greet(name).upper()

print(greet("Jahin"))
print(farewell("Jahin"))
print(shout("Jahin"))
