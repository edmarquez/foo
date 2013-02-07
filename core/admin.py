from django.contrib import admin
from todo.core.models import *

admin.site.register(todo, todoAdmin)
