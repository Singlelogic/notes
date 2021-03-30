from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Bb, Rubric
from .forms import BbForm


class BbCreateView(CreateView):
    # Атрибут, задает ссылку на класс модели, на основе которой будет создана форма
    model = Bb
    # ссылка на класс формы, связанной с моделью;
    form_class = BbForm

    # Атрибут, указывает последовательность имен полей модели, который должны
    # присутствовать в форме. Можно указать либо модель и список ее полей
    # в атрибутах model и fields, либо непостедственно класс формы
    # в атрибуте form_class, но никак не одновременно и то, и другое.
    # Если указан атрибут model, то обязательно слудует задать также и
    # атрибут fields.
    # fields = ['title', 'content', 'price', 'kind', 'rubric']

    # путь к файлу шаблона, создающего страницу с формой;
    # По умолчанию к названии модели добавляется суффикс '_form',
    # В данном случает будет 'bb_form'.
    template_name = 'bboard/bb_create.html'

    # Атрибут, хранящий словарь с изначальными данными для занесения в только
    # что созданную форму. Ключи элементов этого словаря должны
    # соответствовать полям формы, а значения элементов зададут значения полей
    initial = {'price': 0.0}

    # интернет-адрес для перенаправления после успешного сохранения данных;
    success_url = reverse_lazy('bb_list_url')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['rubrics'] = Rubric.objects.all()
        return context


class BbDetailView(DetailView):
    # Задает модель (обязателен к заполнению)
    model = Bb
    # Если не указан путь к шаблону - значит, класс будет искать шаблон
    # со сформированныйм по умолчанию путем.
    # В данном примере будет путь 'bb_detail.html'
    template_name = None
    # Задает имя поля модели, в котором хранится слаг (по умолчанию: 'slug')
    slug_field = 'slug'
    # Задает имя URL-параметра, через который контроллер-класс получит
    # слаг (по умолчанию: 'slug')
    slug_url_kwarg = 'slug'
    # Задает июя URL-параметра, через который контроллер-класс получит
    # ключ записи (по умолчанию: 'pl')
    pk_url_kwarg = 'pk'
    # Задает имя переменной контекста шаблона, в которой будет сохранена
    # найденная запись.
    # По умолчанию в контексте шаблона будет создана переменная с названием
    # класса модели, в данном случае будет созданна переменная bb,
    # хранящая найденную запись, а также переменную object, чтобы успешно
    # работали наследуемые им примеси.
    context_object_name = None

    # Переопределеный метод, если требуется что-то добавить в контекст шаблона.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbListView(ListView):
    model = Bb
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['rubrics'] = Rubric.objects.all()
        return context


class BbByRybricView(ListView):
    # Если не указан путь к шаблону - значит, класс будет искать шаблон
    # со сформированныйм по умолчанию путем.
    # В данном примере будет путь 'bb_list.html'
    template_name = 'bboard/bb_by_rubric.html'
    # Задает имя переменной контекста шаблона, в которой будет сохранена
    # найденная запись.
    context_object_name = 'bbs'
    # Атрибут, задающий целочисленное количество записей в одной части паринатора.
    # Если не указан или его значение равно None, набор записей
    # не будет разбиваться на части.
    paginate_by = 2

    # Указывает либо диспечер записей (Manager), либо исходный набор
    # записей (QuerySet), из которого будут извлекаться записи.
    # queryset = None

    # Атрибут, хранящий строку с суфиксом, который будет добавлен к
    # автоматически сгенерированному пути к шаблону (по умолчанию: '_list').
    # template_name_suffix = '_list'

    # template_engine = None
    # response_class = TemplateResponse
    # content_type = None

    # Атрибут. Значение True разрешает извлечение 'пустой', т.е. не содержащей
    # ни одной записи, части пагинатора (поведение по умолчанию).
    # Значение False, напротив, предписывает при попытке извленчения 'пустой'
    # части возбуждать исключение Http404.
    # allow_empty = True

    # Атрибут, задающий целочисленное минимальное число записей, которые могут
    # присутствовать в последней части пагинатора.
    # Если последняя часть пагинатора содержит меньше записей,
    # то оставшиеся запису будут выведены в предыдущей части.
    # Если задать значение 0, то в последней части может присутствовать сколько
    # угодно записей (поведение по умолчани).
    # paginate_orphans = 0

    # Атрибут, указывающий класс используемого пагинатора
    # (по умолчанию: Paginator из модуля django.core.paginator).
    # paginator_class = Paginator

    # Указыввает имя URL- или GET-параметра, через который будет передаваться
    # номер выводимой части пагинатора, в виде строки (по умолчанию: "page").
    # page_kwarg = 'page'

    # Задает параметры сортировки записей. Значение может быть указано в виде:
    #    - строки с именем поля, для сортироваки толдько по этому полю.
    # По умолчанию будет выполняться сортировака по возврастанию значения поля.
    # Чтобы указать сортировку по убыванию, нужно предварить имя поля
    # символом "минус".
    #    - последовательности строк с именами полей - для сортировки сразу
    # по нескольким полям.
    # ordering = None

    # Метод, возвращает исходый набор записей (QuerySet),
    # из которого будут извлекаться записи.
    def get_queryset(self):
        return Bb.objects.filter(rubric=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] =  Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(
                                            pk=self.kwargs['pk'])
        return context


class BbUpdateView(UpdateView):
    # Задает модель
    model = Bb

    # Атрибут, указывает последовательность имен полей модели, который должны
    # присутствовать в форме. Можно указать либо модель и список ее полей
    # в атрибутах model и fields, либо непостедственно класс формы
    # в атрибуте form_class, но никак не одновременно и то, и другое.
    # Если указан атрибут model, то обязательно слудует задать также и
    # атрибут fields.
    fields = ('title', 'content', 'price', 'kind', 'rubric')

    # Путь к файлу шаблона, создающего страницу с формой;
    # По умолчанию к названии модели добавляется суффикс '_form',
    # В данном случает будет 'bb_form'.
    template_name = 'bboard/bb_update.html'

    # интернет-адрес для перенаправления после успешного сохранения данных;
    success_url = reverse_lazy('bb_list_url')

    # Задает имя поля модели, в котором хранится слаг (по умолчанию: 'slug')
    # slug_field = 'slug'

    # Задает имя URL-параметра, через который контроллер-класс получит
    # слаг (по умолчанию: 'slug')
    # slug_url_kwarg = 'slug'

    # Задает июя URL-параметра, через который контроллер-класс получит
    # ключ записи (по умолчанию: 'pl')
    # pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbDeleteView(DeleteView):
    # Задает модель
    model = Bb

    # Путь к файлу шаблона, создающего страницу с формой;
    # По умолчанию к названии модели добавляется суффикс '_confirm_delete',
    # В данном случает будет 'bb_confirm_delete'.
    template_name = 'bboard/bb_delete.html'

    # интернет-адрес для перенаправления после удаления;
    success_url = reverse_lazy('bb_list_url')

    # Задает имя поля модели, в котором хранится слаг (по умолчанию: 'slug')
    # slug_field = 'slug'

    # Задает имя URL-параметра, через который контроллер-класс получит
    # слаг (по умолчанию: 'slug')
    # slug_url_kwarg = 'slug'

    # Задает июя URL-параметра, через который контроллер-класс получит
    # ключ записи (по умолчанию: 'pl')
    # pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
