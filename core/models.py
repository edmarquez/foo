from django.db import models
from django.contrib import admin


CATEGORIAS_CHOICE = (
	('nuevo', 'Nuevo'),
	('trabajo', 'Trabajo'),
	('hogar', 'Hogar'),
	('vacacion', 'Vacacion'),
)

class todo(models.Model):
	name = models.CharField(max_length=100, unique=True)
	categorias = models.CharField(max_length=20, choices=CATEGORIAS_CHOICE, default='nuevo' )
	description = models.TextField()
	created = models.DateTimeField()

	def __unicode__(self):
		return self.name

class todoAdmin(admin.ModelAdmin):
	date_hierachy = 'created'
	list_filter = ('categorias', )
	list_display = ('name', 'categorias', 'created')
	search_field = ['decription']
