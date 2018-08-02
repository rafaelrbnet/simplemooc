from django.urls import path
from simplemooc.courses import views as courses_views

app_name = 'courses'

urlpatterns = [
    path('', courses_views.index, name='index'),
    path('<slug:slug>', courses_views.details, name='details'),
    path('<slug:slug>/inscricao/', courses_views.enrollment, name='enrollment'),
    path('<slug:slug>/cancelar-inscricao/', courses_views.undo_enrollment, name='undo_enrollment'),
    path('<slug:slug>/anuncios/', courses_views.announcements, name='announcements'),
    path('<slug:slug>/informacoes/', courses_views.show_details, name='show_details'),
    path('<slug:slug>/anuncios/<pk>', courses_views.show_announcement, name='show_announcement'),
    path('<slug:slug>/aulas/', courses_views.lessons, name='lessons'),
    path('<slug:slug>/aulas/<pk>', courses_views.show_lesson, name='show_lesson'),
    path('<slug:slug>/materiais/<pk>', courses_views.material, name='material'),
]