from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Place


class CreatePlaceView(CreateView):
    template_name='create.html'
    model = Place
    succes_url = reverse_lazy('/')
    fields=['title', 'description', 'location']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePlaceView, self).form_valid(form)
