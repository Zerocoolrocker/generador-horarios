from .models import Materia, MateriaSeccion, Bloque, Horario, MateriaHorario


def generar_horarios():
	#lista de codigos de las materias a inscribir
	materias_inscribir = '__all__'
	

	materiasSeccion = MateriaSeccion.objects.all() if materias_inscribir == '__all__' else MateriaSeccion.objects.filter(code__in=materias_inscribir)
	#ordena materias por seccion
	materiasSeccion = sorted(materias, key=lambda mat: mat.seccion)

	cns = [0] * len(materias)



	while True:

		#@TODO: Backtrackig
		horario = []

		#Guardar Horario
		if horario:
			hor = Horario()
			hor.save()
			for mat in materiasSeccion:
				MateriaHorario(
					horario=hor,
					seccion_materia=mat
				).save()





		else:
			break
