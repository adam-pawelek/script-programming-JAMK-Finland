countrycodes = ["fi", "se", "no"]

codemap = {
	"fi" : "finland",
	"se" : "sweden",
	"no" : "norway",
}


countries ={
	'finland' : {'head honcho' : ("Juha Sipila",   54), 'population' : 5.439},
	'sweden'  : {'head honcho' : ("Stefan Lofven", 58), 'population' : 9.593},
	'norway'  : {'head honcho' : ("Erna Solberg",  54), 'population' : 5.084},

}



for i in range (len (countrycodes)):
	myCountry = codemap[countrycodes[i]]
	print(myCountry + ":")
	print ('\t' + "head honcho: " + str (countries[myCountry]['head honcho'][0]) + ", who is " +  str (countries[myCountry]['head honcho'][1]) + " years old"   )
	print ('\t' + "population: " +  str (countries[myCountry]['population'] )+ " million")



'''
for i in range (len (countrycodes)):
	myCountry = codemap[countrycodes[i]]
	countt = 0
	print(myCountry + ":")
	for j in countries[myCountry]:
		if countt == 0:	
			print ('\t' + j + " " + str (countries[myCountry][j][0]) + ", who is " +  str (countries[myCountry][j][1]) + " years old"   )
			countt+=1
		else:
			print ('\t' + j +" " +  str (countries[myCountry][j] )+ " million")

	'''		

