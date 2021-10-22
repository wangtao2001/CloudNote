from django.urls import path, include
from . import views

urlpatterns = [
    path('all_note', views.all_note_view),
    path('add_note', views.add_note_view),
    path('delete_note/<int:note_id>', views.delete_note),
    path('detail_note/<int:note_id>', views.detail_note_view),
    path('update_note/<int:note_id>', views.update_note_view)
]
