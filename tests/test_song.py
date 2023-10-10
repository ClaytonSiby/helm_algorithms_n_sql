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

        assert first.is_repeating_playlist() is False
        assert second.is_repeating_playlist() is False

        first.next_song(second)
        second.next_song(first)

        assert first.is_repeating_playlist() is True
        assert second.is_repeating_playlist() is True

    def test_song_with_same_name(self):
        song_one = Song("Hello")
        song_two = Song("Hello")

        assert song_one.is_repeating_playlist() is False
        assert song_two.is_repeating_playlist() is False

        song_one.next_song(song_two)

        assert song_one.is_repeating_playlist() is True
