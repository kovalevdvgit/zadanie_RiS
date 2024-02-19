from django.shortcuts import render
#from bird.models import
from bird.forms import BirdForm
from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from bird.models import bird, view_bird
import datetime

seen_bird = None

# Create your views here.
def create_bird(request):
    if request.method == 'POST':
        form = BirdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_bird')
    else:
        template = loader.get_template('create_bird.html')
        form = BirdForm()

    contextlib = {'form':form}
    return HttpResponse(template.render(contextlib, request))

class all_bird(ListView):
    template_name = 'all_bird.html'
    model = bird

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if seen_bird:
            context['seen'] = True
        return context

def func_view_bird(request, pk):
    template = loader.get_template('view_bird.html')
    select_bird = bird.objects.get(pk=pk)
    context = {'object':select_bird}
    if request.method == 'POST':
        global seen_bird
        create_view_bird = view_bird()
        create_view_bird.bird = select_bird
        create_view_bird.save()
        seen_bird = select_bird

    return HttpResponse(template.render(context, request))

def func_recently_view(request):
    template = loader.get_template('recently_view.html')
    context = {'object': None
               }
    if request.method == 'POST':

        if seen_bird:
            quantity_view = len(seen_bird.view_bird_set.all())
            #date_last_view = seen_bird.view_bird_set.all().last().date
            date_last_view = datetime.datetime.now()
            context = {'object': seen_bird,
                       'quan': quantity_view,
                       'date': date_last_view,
                       }
        else:
            context = {'object': 'blank'
                       }

    return HttpResponse(template.render(context, request))




