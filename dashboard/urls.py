from django.urls import path, include
from . import views
from .views import index, print_pdf_with_selection, delete_selected_favorites

app_name = 'dashboard'

urlpatterns = [
    path('', index, name='index'),
    path('print-pdf-with-selection/', print_pdf_with_selection, name='print_pdf_with_selection'),
    path('delete-selected-favorites/', delete_selected_favorites, name='delete_selected_favorites'),

]
