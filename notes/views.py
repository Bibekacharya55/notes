from django.shortcuts import render
from .models import Note
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from .forms import EditForm,ProductForm
from django.db.models import Q   #we can use it in complex queries or or lookup
# Create your views here.

class Note_list(ListView): 
    model = Note
    template_name='notes_list.html'
    # context_object_name = 'search_list'

    # def get_queryset(self):
    #     queryset= super.get_queryset
    #     query = self.request.GET('q')

    #     if query:
    #         queryset = queryset.filter(Q(title_icontains=query) | Q(content_icontains=query)).distinct()
    #     return queryset
    
        
class Note_detail(DetailView):
    model = Note
    template_name='notes_detail.html'


class Note_create(CreateView):
    model = Note
    template_name = 'notes_create.html'
    success_url = reverse_lazy('list')
    form_class = ProductForm
    
    

class Note_edit(UpdateView):
    model = Note
    template_name = 'notes_edit.html'
    success_url = reverse_lazy('list')
    form_class = EditForm

class Notedelete(DeleteView):
    model = Note
    success_url = reverse_lazy('list')
    template_name = 'confirmdelete.html'

class Notesearch(ListView):
    model = Note
    template_name = 'notes_list.html'
    context_object_name = 'search_list'

    def get_queryset(self):
        queryset= super.get_queryset
        query = self.request.GET('q')

        if query:
            queryset = queryset.filter(Q(title_icontains=query) | Q(content_icontains=query)).distinct()
            return queryset
   

