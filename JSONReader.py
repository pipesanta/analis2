#########Autores Colab#########
import json
from Author import  Author
from Article import  Article

with open("university_of_antioquia.json",encoding="utf-8") as dataUdeA: 
    articles=json.loads(dataUdeA.read())



def agregarColab(autor):
	losAutores=[]
	colabs=[]
	autorPpal=[]
	for article in articles:
		losAutores= article.get('Author').get('s').split(';')
		if autor.lower() in losAutores[0].lower():
			autorPpal=losAutores[0]
			colabs=losAutores[1:]
			articulo= article.get('Title')
			pais=article.get('Journal Country')
			temas=article.get('Fields of Study')
			if pais == "":
				pais="pais desconocido"
	if not autorPpal:
		print("No existe el autor")
		return
	if not colabs:
		print("El autor: "+autorPpal+" de "+pais+ " no tiene colaboraciones")
		print("Trabajo en: "+articulo+"\nEn los siguientes temas: "+temas)
		return
	print("El autor: "+autorPpal+" de "+pais+ "\nColaboro con: "+str(colabs))
	print("En el articulo :"+" "+articulo+"\nEn los siguientes temas: "+temas)	

def searchAuthor(autor):
	losAutores=[]
	colabs=[]
	autorPpal=[]
	for article in articles:
		losAutores= article.get('Author').get('s').split(';')
		if autor.lower() in losAutores[0].lower():

			autorPpal= Author(losAutores[0], '', '')
			colabs=losAutores[1:]
			collaborators = []
			for collaborator in colabs:
				collaborators.append(Author(collaborator, '', ''))
			
			articulo= article.get('Title')
			pais=article.get('Journal Country')
			temas=article.get('Fields of Study')
			if pais == "":
				pais="pais desconocido"
	if not autorPpal:
		print("No existe el autor")
		return
	if not colabs:

		print("El autor: "+autorPpal+" de "+pais+ " no tiene colaboraciones")
		print("Trabajo en: "+articulo+"\nEn los siguientes temas: "+temas)
		return
	# print("El autor: de "+pais+ "\nColaboro con: "+str(colabs))

	autorPpal.print()


	print("En el articulo :"+" "+articulo+"\nEn los siguientes temas: "+temas)
		

autorNombre= input("Ingrese nombre del Autor a consultar: " )
# agregarColab(autorNombre)

agregarColab(autorNombre)

