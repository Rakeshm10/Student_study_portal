from django.shortcuts import render,redirect , get_object_or_404 
from django.contrib import messages  # Import messages module

from . forms import *
from django.contrib import messages
from django.views import generic, View

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Assignment
from .forms import AssignmentForm
from .forms import UploadPdfForm




from youtubesearchpython import VideosSearch

import requests


def home(request):
    return render(request,'Dashboard/home.html')




# notes

def notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, f"Notes added from {request.user.username} successfully")
            return redirect('notes') 
           
    else:
        form = NotesForm()
    user_id = request.user.id if request.user.is_authenticated else None
    notes = Notes.objects.filter(user_id=user_id)
    # notes = Notes.objects.filter(user=request.user)
    context = {'notes': notes, 'form': form}
    return render(request, 'Dashboard/notes.html', context)




def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")


class    NotesDetailView(generic.DetailView):
    model= Notes







# Assignment

def assignments_list(request):
    if request.method =="POST":
        form =AssignmentForm(request.POST)

        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished =='on':
                    finished=True
                else:
                    finished=False
            except:
                finished=False

            assignments=Assignment(
                user=request.user,
                subject=request.POST['subject'],
                title=request.POST['title'],
                description=request.POST['description'],
                due=request.POST['due'],
                is_finished=finished

            )
            assignments.save()
            messages.success(request,f"Assignments added from{request.user.username} !!")
    else:
        form= AssignmentForm()
    assignments = Assignment.objects.filter(user=request.user)
    if len(assignments)==0:
        assignment_done =True
    else:
        assignment_done =False
     
    context = {'assignments': assignments, 
               'assignments_done': assignment_done,
               'form':form,
               }
    return render(request, 'Dashboard/Assignments.html', context)




#upload pdf
class UploadPdfView(View):
    template_name = 'upload_pdf.html'

    def get(self, request, *args, **kwargs):
        assignment_id = self.kwargs.get('pk')  # Extract 'pk' from kwargs
        assignment = get_object_or_404(Assignment, pk=assignment_id)
        return render(request, 'Dashboard/upload_pdf.html', {'assignment': assignment})

    def post(self, request, *args, **kwargs):
        assignment_id = self.kwargs.get('pk')  # Extract 'pk' from kwargs
        assignment = get_object_or_404(Assignment, pk=assignment_id)
        form = UploadPdfForm(request.POST, request.FILES, instance=assignment)

        if form.is_valid():
            form.save()
            uploaded_file = assignment.file_field
            return render(request, 'Dashboard/upload_pdf.html', {'assignment': assignment, 'form': form, 'uploaded_file': uploaded_file})
  
            # return redirect("assignments_list")

        return render(request, 'Dashboard/upload_pdf.html', {'assignment': assignment, 'form': form})


def delete_assignment(request,pk=None):
    Assignment.objects.get(id=pk).delete()
    return redirect("assignments_list")

def update_assignment(request,pk=None):
    assignment= Assignment.objects.get(id=pk)
    if assignment.is_finished == True:
        assignment.is_finished == False
    else:
        assignment.is_finished == True
    assignment.save()
    return redirect('assignments_list')







#youtube

def youtube(request):
        if request.method == "POST":
            form = DashoardForm(request.POST)
            text = request.POST['text']
            video=VideosSearch(text,limit=20)
            result_list = []
            for i in video.result()['result']:
                result_dict ={
                    'input':text,
                    'title':i['title'],
                    'duration':i['duration'],
                    'thumbnail':i['thumbnails'][0]['url'],
                    'channel':i['channel']['name'],
                    'link':i['link'],
                    'views':i['viewCount']['short'],
                    'published':i['publishedTime']

                }

                desc = ' '
                if i['descriptionSnippet']:
                    for j in i['descriptionSnippet']:
                        desc += j['text']
                result_dict['description']= desc
                result_list.append(result_dict)
                context ={
                    'form': form,
                    'results':result_list
                }
            
            return render(request,'Dashboard/youtube.html',context)
        else:
            form = DashoardForm()
        context= {'form': form}
        return render(request, 'Dashboard/youtube.html',context)




#register
def register(request):
    if request.method == 'POST':
        form= UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account has been created")
            return redirect("login")

    else:
        form = UserRegistrationForm()


    return render(request, 'Dashboard/register.html', {'form': form})







#Ebooks

def books(request):
    if request.method == "POST":
        form = DashoardForm(request.POST)
        text = request.POST['text']
        url = "https://www.googleapis.com/books/v1/volumes?q=" + text
        r = requests.get(url)

        if r.status_code == 200:
            answer = r.json()
            result_list = []

            if 'items' in answer and len(answer['items']) > 0:
                for i in range(min(10, len(answer['items']))):
                    result_dict = {
                        'title': answer['items'][i]['volumeInfo']['title'],
                        'subtitle': answer['items'][i]['volumeInfo'].get('subtitle'),
                        'description': answer['items'][i]['volumeInfo'].get('description'),
                        'count': answer['items'][i]['volumeInfo'].get('pageCount'),
                        'categories': answer['items'][i]['volumeInfo'].get('categories'),
                        'rating': answer['items'][i]['volumeInfo'].get('pageRating'),
                        'thumbnail': answer['items'][i]['volumeInfo'].get('imageLinks', {}).get('thumbnail'),
                        'preview': answer['items'][i]['volumeInfo'].get('previewLink')
                    }

                    result_list.append(result_dict)
            else:
                result_list = []

            context = {
                'form': form,
                'results': result_list
            }

            return render(request, 'Dashboard/books.html', context)
       
        
    else:
        form = DashoardForm()
        context = {'form': form}
        return render(request, 'Dashboard/books.html', context)







#wikipedia

import wikipedia

from .forms import DashoardForm

def wiki(request):
    if request.method == 'POST':
        text = request.POST['text']
        form = DashoardForm(request.POST)

        try:
            search = wikipedia.page(text)
            context = {
                'form': form,
                'title': search.title,
                'link': search.url,
                'details': search.content  # Use 'content' instead of 'summary for more details
            }
            return render(request, 'Dashboard/wiki.html', context)
        except wikipedia.exceptions.DisambiguationError as e:
            # Handle disambiguation error
            options = e.options
            return render(request, 'Dashboard/choose_option.html', {'form': form, 'options': options})
        except wikipedia.exceptions.PageError as e:
            # Handle page not found error
            return render(request, 'Dashboard/wiki.html', {'form': form, 'error_message': f"Page not found: {e}"})
    else:
        form = DashoardForm()
        return render(request, 'Dashboard/wiki.html', context={'form': form})


def choose_option(request, option):
    # Add your logic for handling the chosen option
    try:
        search = wikipedia.page(option)
        context = {
            'title': search.title,
            'link': search.url,
            'details': search.content
        }
        return render(request, 'Dashboard/wiki.html', context)
    except wikipedia.exceptions.PageError as e:
        return render(request, 'Dashboard/wiki.html', {'error_message': f"Page not found: {e}"})






from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Todo  # Import your Todo model if necessary


#todo
def todo(request):


    form = TodoForm()  # Initialize form instance outside the if block

    if request.method== 'POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            try:
                finished=request.POST["is_finished"]
                if finished=='on':
                    finished= True
                else:
                    finished= False
            except:
                finished= False
            
            todos=Todo(
                user=request.user,
                title=request.POST['title'],
                is_finished=finished
            )
            todos.save()
            messages.success(request,f"Added from {request.user.username}")
        else:
            form=TodoForm()

    todo = Todo.objects.filter(user=request.user)
    if len(todo)==0:
        todos_done= True
    else:
        todos_done= False
    context={
        'form':form,
        'todos':todo,
        'todos_done':todos_done,

    }
    return render(request,"dashboard/todo.html",context)


def update_todo(request,pk= None):
    todo= Todo.objects.get(id=pk)
    if todo.is_finished== True:
        todo.is_finished= False
    else:
        todo.is_finished= True
    todo.save()

    return redirect('todo')



def delete_todo(request,pk= None):
    Todo.objects.get(id=pk).delete()
    return redirect("todo")





#chat
# from django.shortcuts import render
from django.http import JsonResponse
from google.cloud import pubsub_v1
from django.conf import settings



def rooms(request):
    rooms=Room.objects.all()
    return render(request, "dashboard/rooms.html",{"rooms":rooms})

# def room(request,slug):
#     room_name=Room.objects.get(slug=slug).name
#     messages=Message.objects.filter(room=Room.objects.get(slug=slug))
    
#     return render(request, "dashboard/room.html",{"room_name":room_name,"slug":slug,'messages':messages})

from django.shortcuts import get_object_or_404

def room(request, slug):
    room_obj = get_object_or_404(Room, slug=slug)
    room_name = room_obj.name
    messages = Message.objects.filter(room=room_obj)
    
    return render(request, "dashboard/room.html", {"room_name": room_name, "slug": slug, "messages": messages})

