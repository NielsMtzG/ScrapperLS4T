import json
from numpy import dot
from numpy import arccos
from math import pi
import os
def angle(x,y,z):
	angu=[]
	p=[y[0]-x[0],y[1]-x[1]]
	q=[z[0]-x[0],z[1]-x[1]]
	k=dot(p,q)
	j=dot(p,p)**(0.5)
	i=dot(q,q)**(0.5)
	res=(k/(i*j))
	ang1= arccos(res)
	#angu.append(round(ang1,2))
	angu.append(ang1)
	#print(ang1,"ángulo1")
	p=[y[0]-z[0],y[1]-z[1]]
	q=[x[0]-z[0],x[1]-z[1]]
	k=dot(p,q)
	j=dot(p,p)**(0.5)
	i=dot(q,q)**(0.5)
	res=(k/(i*j))
	ang2= arccos(res)
	#angu.append(round(ang2,2))
	angu.append(ang2)
	#print(ang2,"ángulo2")
	#print(pi-ang1-ang2,"ángulo3")
	ang3=pi-ang1-ang2
	#angu.append(round(ang3,2))
	angu.append(ang3)
	#comprobar angulos
	#print("suma de los ángulos=",ang1+ang2+ang3)
	return angu
def brazoIzq(arr):
	#1,2,3,4
	bi1=[]
	bi2=[]
	bi3=[]
	bi0=[]
	res=[]
	bi0.append(arr[3])#1
	bi0.append(arr[4])
	bi1.append(arr[6])#2
	bi1.append(arr[7])
	bi2.append(arr[9])#3
	bi2.append(arr[10])
	bi3.append(arr[12])#4
	bi3.append(arr[13])
	res+=angle(bi1,bi2,bi3)
	res+=angle(bi3,bi1,bi0)
	#ang1=angle(bi1,bi2,bi3)
	return res
def brazoDer(arr):
	#5,6,7,1
	bi1=[]
	bi2=[]
	bi3=[]
	bi0=[]
	res=[]
	bi0.append(arr[3])#puntos 1
	bi0.append(arr[4])
	bi1.append(arr[15])#5
	bi1.append(arr[16])
	bi2.append(arr[18])#6
	bi2.append(arr[19])
	bi3.append(arr[21])#7
	bi3.append(arr[22])
	res+=angle(bi1,bi2,bi3)
	res+=angle(bi3,bi1,bi0)
	#ang1=angle(bi1,bi2,bi3)
	return res
def torso(arr):
	#2,5,8
	bi1=[]
	bi2=[]
	bi3=[]
	bi1.append(arr[6])#2
	bi1.append(arr[7])
	bi2.append(arr[15])#5
	bi2.append(arr[16])
	bi3.append(arr[24])#8
	bi3.append(arr[25])
	res=angle(bi1,bi2,bi3)
	return res
def cabeza(arr):
	#1,17,18
	bi1=[]
	bi2=[]
	bi3=[]
	bi1.append(arr[3])#1
	bi1.append(arr[4])
	bi2.append(arr[51])#17
	bi2.append(arr[52])
	bi3.append(arr[54])#18
	bi3.append(arr[55])
	res=angle(bi1,bi2,bi3)
	return res
def rostro(arr):
	ce11=[]
	ce12=[]
	ce13=[]
	ce21=[]
	ce22=[]
	ce23=[]
	bo11=[]
	bo12=[]
	bo13=[]
	bo21=[]
	bo22=[]
	bo23=[]
	ce11.append(arr[51])
	ce11.append(arr[52])
	ce12.append(arr[57])
	ce12.append(arr[58])
	ce13.append(arr[63])
	ce13.append(arr[64])
	angC1=angle(ce11,ce12,ce13) #ceja izquierda imagen
	ce21.append(arr[66])
	ce21.append(arr[67])
	ce22.append(arr[72])
	ce22.append(arr[73])
	ce23.append(arr[78])
	ce23.append(arr[79])
	angC2=angle(ce21,ce22,ce23) #ceja derecha imagen
	bo11.append(arr[153])
	bo11.append(arr[154])
	bo12.append(arr[21])
	bo12.append(arr[22])
	bo13.append(arr[27])
	bo13.append(arr[28])
	angC3=angle(bo11,bo12,bo13) #Boca Nariz
	bo21.append(arr[171])
	bo21.append(arr[172])
	bo22.append(arr[147])
	bo22.append(arr[148])
	bo23.append(arr[159])
	bo23.append(arr[160])
	angC4=angle(bo21,bo22,bo23) #Boca labios
	res=angC1+angC2+angC3+angC4
	return res

def mano(arr): #pasar como arr el izquierdo o derecho, funciona igual..
	d11=[] #menique
	d12=[]
	d13=[]
	d21=[] #anular
	d22=[]
	d23=[]
	d31=[] #medio
	d32=[]
	d33=[]
	d41=[] #indice
	d42=[]
	d43=[]
	d51=[] #pulgar
	d52=[]
	d53=[]
	d11.append(arr[60])
	d11.append(arr[61])
	d12.append(arr[57])
	d12.append(arr[58])
	d13.append(arr[54])
	d13.append(arr[55])
	angD1=angle(d11,d12,d13)
	d21.append(arr[48])
	d21.append(arr[49])
	d22.append(arr[45])
	d22.append(arr[46])
	d23.append(arr[42])
	d23.append(arr[43])
	angD2=angle(d21,d22,d23)
	d31.append(arr[36])
	d31.append(arr[37])
	d32.append(arr[33])
	d32.append(arr[34])
	d33.append(arr[30])
	d33.append(arr[31])
	angD3=angle(d31,d32,d33)
	d41.append(arr[24])
	d41.append(arr[25])
	d42.append(arr[21])
	d42.append(arr[22])
	d43.append(arr[18])
	d43.append(arr[19])
	angD4=angle(d41,d42,d43)
	d51.append(arr[12])
	d51.append(arr[13])
	d52.append(arr[9])
	d52.append(arr[10])
	d53.append(arr[6])
	d53.append(arr[7])
	angD5=angle(d51,d52,d53)
	res=angD1+angD2+angD3+angD4+angD5
	return res


#f = open("./32_keypoints.json")
def archi(f):
	data = json.load(f)
	tupla=[]
	maniz=data['people'][0]['hand_left_keypoints_2d']#izquierda
	mander=data['people'][0]['hand_right_keypoints_2d']#derecha
	pose=data['people'][0]['pose_keypoints_2d']#pose
	cara=data['people'][0]['face_keypoints_2d']#rostro
	frame = data
	biz=brazoIzq(pose) #regresa 2
	tupla+=biz
	bder=brazoDer(pose) #regresa 2
	tupla+=bder
	tupla+=torso(pose) #regresa 1
	tupla+=cabeza(pose) #regresa 1
	return tupla
	#return pose
	#insertar código de obtención de angulos...

#-----Main---// este script solo toma en cuenta los valores de la pose
"""
path = "./exaM/"
dir_list = os.listdir(path)
lista=[] #elementos a borrar
f=1
for i in dir_list:
	if (i[0]!='.'):
		imp=path+i
		f = open(imp)
		obs=archi(f)
		lista.append(obs)
#crear el archivo
nv=len(lista[0])
cab=[]
for i in range(0,nv):
	cab.append('var '+str(i))

salida=open("./base3.csv","w")
salida.write(",".join(cab)+'\n')

for j in lista:
	#print(j)
	x = ",".join(str(v) for v in j)
	salida.write(x+'\n')
"""
#f = open("./1/6_keypoints.json")
#f = open("./2/2_keypoints.json")
#f = open("./3/5_keypoints.json")
#f = open("./4/5_keypoints.json")
#f=open("./exaM/46_keypoints.json")
#f=open("./5/27_keypoints.json")
#f=open("./6/70_keypoints.json")
f=open("./myoutputv1/976_keypoints.json")
print(archi(f))