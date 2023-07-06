from django.shortcuts import redirect
from django.views import View
from django.shortcuts import render
from .models import Make, CarModel, Collection
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DeleteView
from django.urls import reverse

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["collections"] = Collection.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"

class MakeCreate(CreateView):
    model = Make
    fields = ['name', 'image', 'country']
    template_name = "make_create.html"
    success_url = '/makes/'

class MakeList(TemplateView):
    template_name = "make_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context["makes"] = Make.objects.filter(name__icontains=name)
        else:
            context["makes"] = Make.objects.all()
        return context

class MakeDetail(DeleteView):
    model = Make
    template_name = "make_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["collections"] = Collection.objects.all()
        return context


class MakeUpdate(UpdateView):
    model = Make
    fields = ['name', 'image', 'country']
    template_name = "make_update.html"
    success_url = "/makes/"

    def get_success_url(self):
        return reverse('make_detail', kwargs={'pk': self.object.pk})

class MakeDelete(DeleteView):
    model = Make
    template_name = "make_delete_confirmation.html"
    success_url = "/makes/"

class CarModelCreate(View):

    def post(self, request, pk):
        name = request.POST.get("name")
        price = request.POST.get("price")
        make = Make.objects.get(pk=pk)
        image = request.POST.get("image")
        CarModel.objects.create(name=name, price=price, make=make, image=image)
        return redirect('make_detail', pk=pk)

class CollectionCarModelAssoc(View):

    def get(self, request, pk, carmodel_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            Collection.objects.get(pk=pk).carmodels.remove(carmodel_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            Collection.objects.get(pk=pk).carmodels.add(carmodel_pk)
        return redirect('home')
