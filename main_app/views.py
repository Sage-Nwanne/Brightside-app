from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


from .models import Entry, MOODS, Comments
from .forms import CommentForm

# Define the home view function
class Home(LoginView):
    template_name = 'home.html'
          

def about(request):
    return render(request, 'about.html')

def entries(request):
    is_archived = request.GET.get('is_archived', False)
    is_archived = is_archived.lower() == 'true' if isinstance(is_archived, str) else False
    
    user_entries = Entry.objects.filter(
        user=request.user,
        is_archived=is_archived
    ).order_by('-created_at')
    
    for entry in user_entries:
        mood_key = entry.mood
        entry.mood_data = MOODS[mood_key]

    template = 'entries/archived-entries.html' if is_archived else 'entries/index.html'
    return render(request, template, {
        'entries': user_entries
    })
    
def entries_detail(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    mood_key = entry.mood
    entry.mood_data = MOODS[mood_key]
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.entry = entry
            comment.user = request.user
            comment.save()
            return redirect('entry-detail', entry_id=entry_id)
    else:
        form = CommentForm()

    return render(request, 'entries/details.html', {
        'entry': entry,
        'form': form
    })


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('entries')  # Changed from 'cat-index' to 'entries'
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)  # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )








class EntriesCreate(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ['title', 'content', 'mood', 'is_archived']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EntriesUpdate(UpdateView):
    model = Entry
    fields = ['title', 'content', 'mood', 'is_archived']

class EntriesDelete(DeleteView):
    model = Entry
    success_url = '/entries'

def archive_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    entry.is_archived = not entry.is_archived
    entry.save()
    return redirect('entry-detail', entry_id=entry_id)
    

def add_comment(request, entry_id):
    if request.method == 'POST':
        entry = Entry.objects.get(id=entry_id)
        new_comment = Comments.objects.create(
            content=request.POST['content'],
            entry=entry,
            user=request.user
        )
        return redirect('entry-detail', entry_id=entry_id)
    return redirect('entry-detail', entry_id=entry_id)
