from booking import Booking
from hotel import Hotel
from room import Room


hotel = Hotel()


def create(type, name):
    room = Room(name)
    hotel.add_room(room)


def book(room_id, start, end):
    date_start = int(start)
    date_end = int(end)
    room = hotel.find_room(int(room_id))
    if (not room.valid_date(date_start, date_end) or (date_start > date_end)):
        return
    booking=Booking(date_start, date_end)
    room.book(booking)


def cancel(booking_id):
    hotel.cancel_booking(int(booking_id))


switch_dict={
    "create": create,
    "book": book,
    "cancel": cancel
}

no_line=int(input())

for i in range(no_line):
    user_input=input().split()
    selected_function=switch_dict.get(user_input[0])
    args=user_input[1:]
    selected_function(*args)

for room in hotel.rooms:
    print("Room: %s" % room.name)
    for booking in room.bookings:
        print("Booking Id %s: %s -> %s" % (booking.get_id(),booking.start,booking.end))
