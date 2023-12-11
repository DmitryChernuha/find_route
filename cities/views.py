from django.core import paginator
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from cities.forms import CityForm
from cities.models import City


def home(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    qs = City.objects.all()
    form = CityForm()
    lst = Paginator(qs, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    model = City
    template_name = 'cities/detail.html'


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')


class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')


class CityListView(ListView):
    model = City
    paginate_by = 5
    template_name = 'cities/home.html'




