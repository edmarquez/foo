# Create your views here.
from todo.core.models import todo
from django.shortcuts import render_to_response

def index(request):
	items = todo.objects.all()
	return render_to_response('todo_view.html', {'items':items})
