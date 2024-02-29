animal = "chaNcho feliz"
animal2 = " chancho python "

print(animal.upper())
print(animal.lower())
print(animal2.strip().capitalize())
print(animal.title())
print(animal2.strip()) # remueve espacios
print(animal.rstrip()) # remueve espacios a la derecha
print(animal.find("ch")) #este metodo devuelve el indece de la cadena
print(animal.find("felix")) # si no es}xite el carecter en cuestion me va aparecer un -1 de no lo encuentro  y si es positivo lo consigue
print(animal.replace("ch", "fe")) # reemmplaza la el valor 
print("ch" in animal) # esta validando si se encuentra te retorna un booleano 
print("cha" not in animal) # valida sin no esta te retorna un booleno 

