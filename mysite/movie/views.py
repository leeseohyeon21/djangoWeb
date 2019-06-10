from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Movie, ScreenTime, Seat, Reservation


def index(request):
    return render(request, 'movie/index.html')


def movieSelect(request, user_id):
    movies = Movie.objects.all()
    context = {'movies': movies, 'user_id':user_id}
    return render(request, 'movie/reservation/movieSelect.html', context)


def screenTimeSelect(request, user_id, movie_id):
    screenTimes = ScreenTime.objects.filter(movieId=movie_id)

    dates = set()
    for screenTime in screenTimes:
        if screenTime.screenDate not in dates:
            dates.add(screenTime.screenDate)

    context = {'screenTimes': screenTimes, 'user_id': user_id, 'movie_id': movie_id, 'dates': dates}
    return render(request, 'movie/reservation/screenTimeSelect.html', context)


def seatSelect(request, user_id, movie_id, screen_id):
    seats = Seat.objects.filter(screenId = screen_id)
    context = {'user_id': user_id, 'seats': seats, 'movie_id': movie_id, 'screen_id': screen_id}
    return render(request, 'movie/reservation/seatSelect.html', context)


def confirm(request, user_id, movie_id, screen_id, seat_id):
    # 좌석 status True 변경
    seat_instance = Seat.objects.get(seatId=seat_id)
    seat_instance.status = True
    seat_instance.save()

    # 예매 번호 설정
    reservation_id = "{}-{}-{}".format(user_id, movie_id, seat_id)

    # 데이터에 row 추가
    try:
        reservation_instance = Reservation.objects.create(
            reservationId = reservation_id,
            username = User.objects.get(username=user_id),
            movieId = Movie.objects.get(movieId=movie_id),
            screenId = ScreenTime.objects.get(screenId=screen_id),
            seatId = Seat.objects.get(seatId=seat_id),
        )
        reservation_instance.save()
    except:
        return seatSelect(request, user_id, movie_id, screen_id)
        
    return render(request, 'movie/reservation/confirm.html', {'user_id': user_id})



def myhistory(request, user_id):
    reservations = Reservation.objects.filter(username=User.objects.get(username=user_id))
    context = {'reservations': reservations, 'user_id': user_id}
    return render(request, 'movie/myhistory.html', context)


def cancel(request, user_id, reservation_id):
    try:
        # 좌석 status False로 변경
        reservation_instance = Reservation.objects.get(reservationId=reservation_id)
        seat_id = reservation_instance.seatId
        seat_instance = Seat.objects.get(seatId=seat_id.seatId)
        seat_instance.status = False
        seat_instance.save()

        # 예매내역 지우기
        reservation_instance.delete()

    except:
        return myhistory(request, user_id)
    
    return myhistory(request, user_id)


def initial(request):
    seats = Seat.objects.all()
    for seat in seats:
        seat.status = False
        seat.save()
    return HttpResponse("성공")