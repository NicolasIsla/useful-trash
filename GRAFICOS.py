import numpy as np
import matplotlib.pyplot as plt

variable=np.arange(1,10,1)
funcion=variable*2
with plt.style.context("bmh"):
	fig, ax = plt.subplots(figsize=(7,3))
	#fig, (ax,ay) = plt.subplots(2,1,figsize=(7,3))
	

	plt.ylabel(" ")
	plt.xlabel(" ")
	plt.suptitle(" ")
	#       areas       
	#verde: #aae6b1
	#azul: #999de0
	#rojo: #e6aab5
	#celeste: #a8e6e3
	#amarillo: #e8e2a9
	ax.fill_between(variable[0:6],funcion[0:6],color="#999de0")
	ax.plot(variable, funcion, 'o--b', label="holi ")
	
	ax.legend(loc="upper right")
	#lower center
plt.show()