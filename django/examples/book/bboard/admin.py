from django.contrib import admin

from .models import Bb, Rubric


class BdAdmin(admin.ModelAdmin):
    # последовательность имен полей, которые должны выводиться в списке записей;
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    # последовательность имен полей, которые должны быть
    # преобразованы в гиперссылки, ведущие на страницу правки записи;
    list_display_links = ('title', 'content')
    # последовательность имен полей, по которым должна выполняться фильтрация;
    search_fields = ('title', 'content')

admin.site.register(Bb, BdAdmin)
admin.site.register(Rubric)
