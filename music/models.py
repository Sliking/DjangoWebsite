from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    logo = models.CharField(max_length=1000)

    def __str__(self):
        return "\nTitle: " + self.title + '\nArtist: ' + self.artist + "\nGenre: " + self.genre + "\n"

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    title = models.CharField(max_length=250)