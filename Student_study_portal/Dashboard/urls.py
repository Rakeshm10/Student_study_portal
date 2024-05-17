from django.urls import path
from . import views

from .views import NotesDetailView
from .views import assignments_list
from .views import UploadPdfView
from .views import choose_option, wiki


# from .views import chat_room


urlpatterns = [
    path('',views.home,name='home'),
    
    path('notes/', views.notes, name='notes'),
    path('delete_note/<int:pk>',views.delete_note,name="delete-note"),
    path('notes_detail/<int:pk>',views.NotesDetailView.as_view(),name="notes-detail"),


    path('Assignments/', views.assignments_list, name='Assignment-list'),
    path('assignments_list/', views.assignments_list, name='assignments_list'),
    path('delete_assignment/<int:pk>/', views.delete_assignment, name='delete-assignment'),
    path('update_assignment/<int:pk>/', views.update_assignment, name='update-assignment'),

    path('youtube/',views.youtube, name='youtube'),
    path('register/', views.register, name='register'),



    path('todo/',views.todo, name='todo'),
    path('update_todo/<int:pk>/', views.update_todo, name='update-todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete-todo'),



    path('books/',views.books, name='books'),


    path('upload-pdf/<int:pk>/',  UploadPdfView.as_view(), name='upload-pdf'),
    # path('chat/<str:room_name>/', views.chat_room, name='chat_room'),

    path('wikipedia/',views.wiki, name='wikipedia'),
    path('choose_option/<str:option>/', choose_option, name='choose_option'),



#chat

   
    path("chat/", views.rooms, name="chat"),
    path("<str:slug>", views.room, name="room"),
   
]

