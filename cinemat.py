import math
class cinematica():
	def __init__(self, tetha1,tetha2, tetha3, distanciaz1, distanciaz2, distanciaz3, alpha1, alpha2, alpha3, distanciax1, distanciax2, distanciax3):
		self.t1 = tetha1
		self.t2 = tetha2
		self.t3 = tetha3
		self.dz1 = distanciaz1
		self.dz2 = distanciaz2
		self.dz3 = distanciaz3
		self.a1 = alpha1
		self.a2 = alpha2
		self.a3 = alpha3
		self.dx1 = distanciax1
		self.dx2 = distanciax2
		self.dx3 = distanciax3

DH =cinematica(0,90,0,2,1,2,0,180,0,1,1,0) #VALOR DE LA DH USANDO LA CLASE cinematica

t1=math.radians(DH.t1)
t2=math.radians(DH.t2)
t3=math.radians(DH.t3)
a1=math.radians(DH.a1)
a2=math.radians(DH.a2)
a3=math.radians(DH.a3)
aa1=DH.dx1
aa2=DH.dx2
aa3=DH.dx3
d1=DH.dz1+DH.dz2
d2=0
d3=DH.dz3
print()

def cinematicas():

	"""	Los atributos de DH=cinematica(self, tetha1,tetha2, tetha3, distanciaz1, distanciaz2, distanciaz3, alpha1, alpha2, alpha3,distanciax1...) hacen referencia a los utilizados en el metodo de Denavit-Hatemberg, donde los angulos ( theta y alpha) deben de estar en grados y las distancias (dz y dx) en metros
          
	   1.- Rotacion alrededor del eje zi-1 un angulo tethai
	   2.- Translacion a lo largo de zi-1 una distancia di
	   3.- Translacion a lo largo de xi una distancia ai
	   4.- Rotacion alrededor del eje xi un angulo ai
 """
pass

print(cinematicas.__doc__)
print()
print("ARTICULACION 1","tetha=", t1,"rad,", "d=", d1,",", "a=", aa1,",", "alpha=", a1)
print("ARTICULACION 2","tehta=", t2,"rad,", "d=", d2,",", "a=", aa2,",", "alpha=", a2)
print("ARTICULACION 3","tetha=", t3,"rad,", "d=", d3,",", "a=", aa3,",", "alpha=", a3)
print()
		
def compute_dh():

	a10=[[math.cos(t1),-math.cos(a1)*math.sin(t1),math.sin(a1)*math.sin(t1), l1*math.cos(t1)],[math.sin(t1),math.cos(a1)*math.cos(t1),-math.sin(a1)*math.cos(t1),l1*math.sin(t1)],[0,math.sin(a1),math.cos(a1),d1],[0,0,0,1]]

a10=[[math.cos(t1),(-1)*math.cos(a1)*math.sin(t1),math.sin(a1)*math.sin(t1), aa1*math.cos(t1)],[math.sin(t1),math.cos(a1)*math.cos(t1),(-1)*math.sin(a1)*math.cos(t1),aa1*math.sin(t1)],[0,math.sin(a1),math.cos(a1),d1],[0,0,0,1]]
a21=[[math.cos(t2),(-1)*math.cos(a2)*math.sin(t2),math.sin(a2)*math.sin(t2), aa2*math.cos(t2)],[math.sin(t2),math.cos(a2)*math.cos(t2),(-1)*math.sin(a2)*math.cos(t2),aa2*math.sin(t2)],[0,math.sin(a2),math.cos(a2),d2],[0,0,0,1]]
a32=[[math.cos(t3),(-1)*math.cos(a3)*math.sin(t3),math.sin(a3)*math.sin(t3), aa3*math.cos(t3)],[math.sin(t3),math.cos(a3)*math.cos(t3),(-1)*math.sin(a3)*math.cos(t3),aa3*math.sin(t3)],[0,math.sin(a3),math.cos(a3),d3],[0,0,0,1]]

matrizf=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
matrizg=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for x in range(0,4):
	for y in range(0,4):
		for z in range(0,4):
			matrizf[x][y]+=a10[x][z]*a21[z][y]
			#print(x,y)


for x in range(0,4):
	for y in range(0,4):
		for z in range(0,4):
			matrizg[x][y]+=matrizf[x][z]*a32[z][y]
print()
print(matrizg)
print()
print(" [[RENGLON 1 MATRIZ [],[],[]],[RENGLON 2 MATRIZ [],[],[]],[RENGLON 3 MATRIZ [],[],[]]")

	
