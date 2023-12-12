from django.views.generic import ListView, DetailView, CreateView, UpdateView

from trains.form import TrainForm
from trains.models import Train


class TrainListView(ListView):
    model = Train
    paginate_by = 5
    template_name = 'trains/trains.html'


class TrainDetailView(DetailView):
    model = Train
    template_name = 'trains/detail.html'


class TrainCreateView(CreateView):
    model = Train
    template_name = 'trains/create.html'
    form_class = TrainForm


class TrainUpdateView(UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'cities/update.html'
