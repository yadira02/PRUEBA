#Declaracion de funciones
def burbuja(a):
	for i in range(1,len(a)-1):
		for j in range(0,len(a)-1):
			if(a[j+1]<a[j]:
				aux=a[j]
				a[j]=a[j+1]
				a[j+1]=aux
	print(a)

#Programa principal
a=[6,5,3,1,8,7,2,4]
print(a)
burbuja(a)
input("Presione enter para continuar")