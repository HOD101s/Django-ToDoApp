from django.shortcuts import render
from .models import MyDo
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def init(request):
	try:
		todo = MyDo.objects.filter(status=False)
	except MyDo.DoesNotExist:
		todo = []

	try:
		done = MyDo.objects.filter(status=True)
	except MyDo.DoesNotExist:
		done = []

	context = {
		'todo_items': todo,
		'done_items': done,
	}

	return render(request, 'app/index.html', context)


@csrf_exempt
def add_todo(request):
	MyDo.objects.create(
		activity=request.POST["content"],
		starttimestamp=timezone.now(),
		endtimestamp=timezone.now(),
	)
	return HttpResponseRedirect("/")


def delete_todo(request, pk):
	MyDo.objects.get(pk=pk).delete()
	return HttpResponseRedirect("/")


def completed_todo(request, pk):
	todo = MyDo.objects.get(pk=pk)
	todo.status = True
	todo.save()
	return HttpResponseRedirect("/")
