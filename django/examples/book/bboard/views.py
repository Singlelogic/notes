from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .forms import BbForm
from .models import Bb, Rubric


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)


class BbCreateView(CreateView):
    # путь к файлу шаблона, создающего страницу с формой;
    template_name = 'bboard/create.html'
    # ссылка на класс формы, связанной с моделью;
    form_class = BbForm
    # интернет-адрес для перенаправления после успешного сохранения данных;
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['rubrics'] = Rubric.objects.all()
        return context


class BbDetailView(DetailView):
    model = Bb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbByRybricView(ListView):
    template_name = 'bboard/by_rubric.html'
    context_object_name = 'bbs'

    def get_queryset(self):
        print(Bb.objects.filter(rubric=self.kwargs['pk']))
        print('Mark_1')
        return Bb.objects.filter(rubric=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        print('Mark_2')
        context = super().get_context_data(**kwargs)
        context['rubrics'] =  Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(
                                            pk=self.kwargs['pk'])
        return context


class BbEditView(UpdateView):
    model = Bb
    form_class = BbForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
