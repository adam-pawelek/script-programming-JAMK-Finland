#from mycode.country_data import *

def funForPrint(codemap,countries,countrycodes):
	for i in range (len (countrycodes)):
		myCountry = codemap[countrycodes[i]]
		print(myCountry + ":")
		print ('\t' + "head honcho: " + str (countries[myCountry]['head honcho'][0]) + ", who is " +  str (countries[myCountry]['head honcho'][1]) + " years old"   )
		print ('\t' + "population: " +  str (countries[myCountry]['population'] )+ " million")