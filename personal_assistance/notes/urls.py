from django.urls import path
from .views import  DeleteView, CustomLoginView, RegisterPage, Notes, Detail, NoteCreate, NoteDelete, NoteUpdate
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('create/', NoteCreate.as_view(), name='create'),
    path('', Notes.as_view(), name='notes'),
    path('note/<int:pk>/', Detail.as_view(), name='detail'),
    path('note-update/<int:pk>/', NoteUpdate.as_view(), name='update'),
    path('note-delete/<int:pk>/', NoteDelete.as_view(), name='delete'),
]