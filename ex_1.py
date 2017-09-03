x2=[[2.3],[0],[24.4],[1]]
a01=[[0.45,1.3,0.94,1.23],[0,0.83,0.2,2.37],[0.2,0.65,0.4,0.3],[0,0,0,1]]
a12=[[1,0.2,0.85,2.467],[0.54,1.3,0,0.77],[0.12,0.68,1,0.8],[0,0,0,1]]
matrizf=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
matriz=[[0],[0],[0],[0]]
for x in range(0,4):
	for y in range(0,4):
		for z in range(0,4):
			matrizf[x][y]+=a01[x][z]*a12[z][y]
			

for y in range(0,4):
 	for z in range(0,4):
        	matriz[y][0]+=matrizf[y][z]*x2[z][0]

print ("MATRIZ TRANSPUESTA", matriz)




