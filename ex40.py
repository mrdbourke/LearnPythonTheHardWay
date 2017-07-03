lyrics = ["25 sitting on 25 mil"]

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
started_from_the_bottom = Song(["Started from the bottom",
                                "Now we here",
                                "Started from the bottom",
                                "Now the whole teams freaking here"])

hyfr = Song(lyrics)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

started_from_the_bottom.sing_me_a_song()

hyfr.sing_me_a_song()
