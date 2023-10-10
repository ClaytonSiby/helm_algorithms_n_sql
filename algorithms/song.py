class Song:
    SONG_NAMES = set()
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

        if self.name in Song.SONG_NAMES:
            return True
        else:
            Song.SONG_NAMES.add(self.name)
        
        return self.next.is_repeating_playlist()
