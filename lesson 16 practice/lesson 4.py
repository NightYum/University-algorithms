class Song:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def total_duration(self):
        total = 0
        for s in self.songs:
            total += s.duration
        return total

    def longest_song(self):
        if not self.songs:
            return None
        return max(self.songs, key=lambda s: s.duration)

p = Playlist()
p.add_song(Song("Solar Drift", 210))
p.add_song(Song("Midnight City", 260))
p.add_song(Song("Neon Dreams", 190))

print(p.total_duration())
l = p.longest_song()
print(l.title, l.duration)