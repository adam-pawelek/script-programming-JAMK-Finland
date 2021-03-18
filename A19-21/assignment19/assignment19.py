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
	print(myCountry)
	print ("population: " +  str (countries[myCountry]['population'] )+ " million")
	print ("Prime minister: " + str (countries[myCountry]['head honcho'][0]) + ", " +  str (countries[myCountry]['head honcho'][1]) + " years old\n"   ) 