class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        
    @classmethod
    def add_song_to_count(self):
        self.count += 1
    @classmethod
    def add_to_genres(self, genre):
        if(not genre in self.genres):
            self.genres.append(genre)
    @classmethod
    def add_to_artists(self, artist):
        if(not artist in self.artists):
            self.artists.append(artist)
    @classmethod
    def add_to_genre_count(self, genre):
        count = self.genre_count.get(genre ,0)
        self.genre_count[genre] = count+1
    @classmethod
    def add_to_artist_count(self, artist):
        count = self.artist_count.get(artist, 0)
        self.artist_count[artist] = count+1



