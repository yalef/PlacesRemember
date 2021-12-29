from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Place


class CreatePlaceView(CreateView):
    template_name = 'create.html'
    model = Place
    success_url = reverse_lazy('home/')
    fields=['title', 'description', 'location']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePlaceView, self).form_valid(form)


class UpdatePlaceView(UpdateView):
   model = Place
   fields = ['title', 'description', 'location']
   success_url = reverse_lazy('home/')
   template_name = 'update.html'


class DeletePlaceView(DeleteView):
    template_name = 'delete.html'
    model = Place
    success_url = reverse_lazy('home')
