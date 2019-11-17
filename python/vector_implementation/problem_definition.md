#Probelm Definition

Implement a class that can represent 2-dimensional vectors. Make sure your class will work
idiomatically with Python's current built-in operators. Specifically your Vector class should:

1. Handle addition
v1 = Vector(1, 1)
v2 = Vector(2, 3)
print(v1 + v2) #  Vector(3, 4)

2. Handle scalar multiplication
print(v1 * 3) # Vector(3, 3)

3. Be consistent with how abs built-in function handles complex numbers (i.e. returns the magnitude)
print(abs(Vector(3, 4))) # 5.0
