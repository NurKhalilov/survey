from django.contrib import admin
from .models import Region, Salesman, Rating, ExtraQuestion, ExtraAnswer, Result


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['region_name', 'slug']
    prepopulated_fields = {'slug': ('region_name',)}


@admin.register(Salesman)
class SalesmanAdmin(admin.ModelAdmin):
    list_display = ['region', 'name', 'surname']
    list_filter = ('region',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['salesman', 'rating', 'purchase_price', 'sent_time']
    list_filter = ('salesman',)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'sent_time']


class ExtraAnswerInline(admin.TabularInline):
    model = ExtraAnswer


@admin.register(ExtraQuestion)
class ExtraQuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'question_type', 'is_active']
    list_editable = ('is_active',)
    inlines = [ExtraAnswerInline]


