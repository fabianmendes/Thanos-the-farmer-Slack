'''
Actuall
'''
#testing

seeds = { "need1" : 0,
		  "need2" : 0,
		  "need3" : None}


def need(number):
	needl = "need" + str(number + 1)
	return needl

class Convertlist(self):
	#

	self = []
	'''TODO. Done: pasar la palabra en sí a una lista!
	Y si dicha palabra se encuentra ya en una lista, 
	'''



def mot1harvest(nro, seeds, cuenta=0):
    global añadidos
    añadidos = set()
    
    for x in range(nro):
       # cuenta = + 1

       seed = need(x) 
       añadir = input("Escriba necesidad nro "+ str(x+1) + " : ")
       añadidos.add(añadir)
       seeds[seed] = añadir
       seeds[seed]= convertlist(seeds[seed])
       
       #print(amarillo)
    
    añadidos = tuple(añadidos)   
    return print(añadidos)
    
    
mot1harvest(3, seeds)
print(seeds)
for x in range(len(añadidos)):
    a = añadidos[x]
    print(a)
    seeds[need(x)] = seeds[need(x)].append(a)
    print(seeds)
