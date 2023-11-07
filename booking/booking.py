import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc
import json
import showtime_pb2_grpc
import showtime_pb2


class BookingServicer(booking_pb2_grpc.BookingServicer):
    def __init__(self):
        with open("{}/data/bookings.json".format("."), "r") as file:
            self.db = json.load(file)["bookings"]

    #this function returns the bookings of the given user (take the userid)
    def GetBookingByUserID(self, request, context):

        for booking in self.db:
            if booking["userid"] == request.user_id:
                yield booking_pb2.BookingData(
                    user_id=booking["userid"], dates=booking["dates"]
                )
    #this function adds a booking of the given user (take the userid)
    def AddBookingForUser(self, request, context):
        is_error = True
        for booking in self.db:
            if booking["userid"] == request.user_id:
                for date_obj in booking["dates"]:
                    if date_obj["date"] == request.date:
                        if request.movie_id not in date_obj["movies"]:
                            with grpc.insecure_channel("localhost:3002") as channel:
                                stub = showtime_pb2_grpc.ShowtimeStub(channel)
                                showtime = stub.GetShowtimeByDate(
                                    showtime_pb2.ShowtimeDate(date=date_obj["date"])
                                )
                                if (len(showtime.movies) != 0) and (
                                    request.movie_id in showtime.movies
                                ):
                                    date_obj["movies"].append(request.movie_id)
                                    is_error = False
                                channel.close()
        if is_error:
            return booking_pb2.BookingData(user_id="user_not_found", dates="")
        else:
            new_bookings = {"bookings": self.db}
            with open("{}/data/bookings.json".format("."), "w") as wfile:
                json.dump(new_bookings, wfile)
            return booking_pb2.BookingData(
                user_id=request.user_id,
                dates=[
                    booking_pb2.MovieDates(date=request.date, movies=[request.movie_id])
                ],
            )
    #this function returns the list of bookings
    def GetListBookings(self, request, context):
        for booking in self.db:
            yield booking_pb2.BookingData(
                user_id=booking["userid"], dates=booking["dates"]
            )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port("[::]:3001")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
