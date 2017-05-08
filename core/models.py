from django.db import models

class Materia(models.Model):
	nombre = models.CharField(max_length=50)
	codigo = models.CharField(max_length=10)
	unidades_credito = models.PositiveIntegerField()

dias = (
	('lun', 1),
	('mar', 2),
	('mie', 3),
	('jue', 4),
	('vie', 5),
	('sab', 6),
	('dom', 7),
)

class MateriaSeccion(models.Model):
	materia = models.ForeignKey(Materia)
	seccion = models.PositiveIntegerField()

	def bloques(self):
		return Bloque.objects.filter(seccion_materia=self)

	def siguiente_seccion(self):
		return Materia.objects.filter(materia=self.materia, seccion__gt=self.seccion).first()

class Bloque(models.Model):
	dia = models.PositiveIntegerField(choices=dias)
	inicio = models.TimeField()
	fin = models.TimeField()
	seccion_materia = models.ForeignKey('MateriaSeccion')
	aula = models.CharField(max_length=10)


class Horario(models.Model):
	pass

	def overlaps(*materiasSeccion):
		"""Dados argumentos de tipo MateriaSeccion, retorna lista de sets de materias cuyos horarios interfieren."""
		res = []
		for mat in materiasSeccion:
			overlaping = set()
			for mat2 in materiasSeccion:
				if mat == mat2:
					pass
				for bloq_mat in mat.bloques:
					for bloq_mat2 in mat2.bloques:
						if (bloq_mat.inicio <= bloq_mat2.inicio and bloq_mat.fin <= bloq_mat2.fin) \
								or (bloq_mat.inicio >= bloq_mat2.inicio and bloq_mat.fin <= bloq_mat2.fin):
							overlaping.add(mat)
							overlaping.add(mat2)
			if overlaping and not overlaping in res:
				res.append(overlaping)
		return res


class MateriaHorario(models.Model):
	horario = models.ForeignKey(Horario)
	seccion_materia = models.ForeignKey('MateriaSeccion')
