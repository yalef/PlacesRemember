from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Place
from django.contrib.auth.mixins import LoginRequiredMixin

class ListPlaceView(LoginRequiredMixin, ListView):
    login_url = 'accounts/login' 
    template_name = 'index.html'
    model = Place
    def get_queryset(self):
        queryset = super(ListPlaceView, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset


class CreatePlaceView(CreateView):
    template_name = 'create.html'
    model = Place
    success_url = reverse_lazy('home')
    fields=['title', 'description', 'location']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePlaceView, self).form_valid(form)


class UpdatePlaceView(UpdateView):
   model = Place
   fields = ['title', 'description', 'location']
   success_url = reverse_lazy('home')
   template_name = 'update.html'


class DeletePlaceView(DeleteView):
    template_name = 'delete.html'
    model = Place
    success_url = reverse_lazy('home')
