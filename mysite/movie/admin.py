from django.contrib import admin
from .models import Movie, ScreenTime, Seat, Reservation


admin.site.register(Movie)
admin.site.register(ScreenTime)
admin.site.register(Seat)
admin.site.register(Reservation)
