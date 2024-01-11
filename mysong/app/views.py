from django.shortcuts import render, redirect,get_object_or_404
from .forms import SongForm, SongUpdateForm
from .models import Song
# Create your views here.

def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('song_list')  # Redirect to a view displaying the list of songs
    else:
        form = SongForm()
    return render(request, 'add_song.html', {'form': form})


# views.py


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})


# def add_songs(request):
#     if request.method == 'POST':
#         form = Song(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('song_list')
#     else:
#         form= Song()
#     return render(request,'add_song.html',{'form':form})

# views.py
# from django.shortcuts import render, get_object_or_404, redirect

# from .forms import SongUpdateForm

def update_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    if request.method == 'POST':
        form = SongUpdateForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_list')  # Redirect to a view displaying the list of songs
    else:
        form = SongUpdateForm(instance=song)

    return render(request, 'update_song.html', {'form': form, 'song': song})
