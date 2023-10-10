class Song:
    song_names = set()
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :return: (bool) True if the playlist is repeating, False otherwise
        """
        if self.next is None:
            return False

        if self.name in Song.song_names:
            return True
        else:
            Song.song_names.add(self.name)
        
        return self.next.is_repeating_playlist()
