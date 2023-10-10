from algorithms.song import Song


class TestSong:
    """
        first = Song("Hello")
        second = Song("Eye of the tiger")

        first.next_song(second)
        second.next_song(first)

        print(first.is_repeating_playlist()) # True
        print(second.is_repeating_playlist()) # True
    """

    def test_song(self):
        first = Song("Hello")
        second = Song("Eye of the tiger")

        first.next_song(second)
        second.next_song(first)

        assert first.is_repeating_playlist() is True
        assert second.is_repeating_playlist() is True

