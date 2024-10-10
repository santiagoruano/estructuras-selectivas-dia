#Simple
a = 33
b = 200


if b > a:
    print(b,"es mayor que ",a)


#Doble

y = 200
z = 333

if y > z:
    print(y,"es mayor que",z)
else:
    print(y,"no es mayor que",z)

#Multiple

c = 200
d = 207
if c > d:
    print(c,"es mayor que",d)
elif c < d:
    print(c,"es menor que",d)
else:
    print(c,"es igual que",d)

#condiciones enlazadas
x = 28

if x > 10:
    print("por encima de diez,")
    if x > 20:
        print("y tambien por encima de 20!")
    else:
        print("pero no por encima de 20.")

# end
print("Estudiar los sabados", end=' ')
print("es genial")

#sep
print("Daniela","Luis","Carlos","Camila")
print("Daniela","Luis","Carlos","Camila", sep="")
print("Daniela","Luis","Carlos","Camila", sep=",")

print("Daniela","Luis","Carlos","Camila", sep = "_", end="_Curso_Python")




