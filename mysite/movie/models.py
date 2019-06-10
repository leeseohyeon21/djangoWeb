from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Movie(models.Model):
    movieId = models.PositiveIntegerField(primary_key=True)
    movieName = models.CharField(max_length=30)

    def __str__(self):
        return self.movieName


class ScreenTime(models.Model):
    screenId = models.CharField(max_length=20, primary_key=True)
    movieId = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screenDate = models.DateField()
    screenTime = models.TimeField()

    def __str__(self):
        return "{0}/{1}".format(self.screenDate, self.screenTime)


class Seat(models.Model):
    seatId = models.IntegerField(primary_key=True)
    screenId = models.ForeignKey(ScreenTime, on_delete=models.CASCADE)
    seatRow = models.IntegerField()
    seatCol = models.CharField(max_length=3)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "{0}{1}".format(self.seatCol, self.seatRow)


class Reservation(models.Model):
    reservationId = models.CharField(max_length=20, primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    screenId = models.ForeignKey(ScreenTime, on_delete=models.CASCADE)
    movieId = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seatId = models.ForeignKey(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return self.reservationId