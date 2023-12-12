from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from trains.form import TrainForm
from trains.models import Train


class TrainListView(ListView):
    model = Train
    paginate_by = 5
    template_name = 'trains/trains.html'


class TrainDetailView(DetailView):
    model = Train
    template_name = 'trains/detail.html'


class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    template_name = 'trains/create.html'
    form_class = TrainForm
    success_url = reverse_lazy('trains:train')
    success_message = 'Поезд успешно создан'


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:train')
    success_message = 'Поезд успешно отредактирован'


class TrainDeleteView(DeleteView):
    model = Train
    success_url = reverse_lazy("trains:train")

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Поезд успешно удален')
        return self.post(request, *args, **kwargs)
