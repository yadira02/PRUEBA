cnt=0
def burbuja(A):
	global cnt
	for i in range(1,len(A)):
			for j in range(0, len(A)-1):
				cnt+=1
				if(A[j+1]<A[j]):
					aux=A[j]
					A[j]=A[j+1]
					A[j+1]=aux
					#print(A)
	return A

#programa principaL
print("ARREGLO DESORDENADO:")
A=[6,5,3,1,8,7,2,4]
print(A)
print("ARREGLO ORDENADO: \n", burbuja(A))
input("presione enter para continuar")