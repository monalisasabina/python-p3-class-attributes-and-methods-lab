class Song:

    count = 0
    genres =[]
    artists = []

    genre_count={}
    artist_count ={}

    
    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count+=increment

    @classmethod
    def add_to_genres(cls,genre):
        if genre not in cls.genres:
          cls.genres.append(genre) 

    @classmethod
    def add_to_artists(cls,artist):
        if artist not in cls.artists:
            cls.artists.append(artist)  

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1        


# ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
# print(ninety_nine_problems.name)
# print(ninety_nine_problems.artist)
# print(ninety_nine_problems.genre)
# print(Song.genre_count)
# print(Song.artist_count)


# ninety_nine_problems = Song("Thriller", "Michael Jackson", "Soul")
# print(ninety_nine_problems.name)
# print(ninety_nine_problems.artist)
# print(ninety_nine_problems.genre)
# print(Song.genre_count)
# print(Song.artist_count)

stuck_on_you = Song("Stuck On You", "Lionel Richie", "Soul")
print(stuck_on_you.name)
print(stuck_on_you.artist)
print(stuck_on_you.genre)
print(Song.genre_count)
print(Song.artist_count)


nakei_nairobi = Song("Nakei Nairobi", "Mbilia Bel", "Rhumba")
print(nakei_nairobi.name)
print(nakei_nairobi.artist)
print(nakei_nairobi.genre)
print(Song.genre_count)
print(Song.artist_count)