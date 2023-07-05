primo = 10000019

def hash(string, a, b, m):
    x = b
    for caracter in string:
        x += ord(caracter) * a
    x %= primo
    x %= m
    return x

palabra = "onomatopeya"
a = 7
b = 3
m = 100

valor_hash = hash(palabra, a, b, m)
print("Valor hash de la palabra:", valor_hash)
