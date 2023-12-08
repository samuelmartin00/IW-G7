from django.shortcuts import render, get_object_or_404, redirect
from .models import Song, Genre, Artist, Album, Satisfaction
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm



def index(request):
    return render(request, 'index.html')

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})

def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'song_detail.html', {'song': song})

def search_songs(request):
    if 'query' in request.GET:
        query = request.GET['query']
        songs = Song.objects.filter(title__icontains=query)  # Filtrar canciones por título
        return render(request, 'song_search.html', {'songs': songs, 'query': query})
    else:
        return render(request, 'song_search.html')

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artist_list.html', {'artists': artists})

def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    return render(request, 'artist_detail.html', {'artist': artist})

# Similarly, add views for Album and Genre

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'album_detail.html', {'album': album})

@login_required
def album_feedback(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.cleaned_data['feedback']
            rating = form.cleaned_data['rating']

            satisfaction = Satisfaction.objects.create(
                album=album,
                user=request.user,
                feedback=feedback,
                rating=rating
            )

            return redirect(to="index")
    else:
        form = FeedbackForm()

    return render(request, "album_feedback.html", {'album': album, 'form': form})

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})

def genre_detail(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    return render(request, 'genre_detail.html', {'genre': genre})
