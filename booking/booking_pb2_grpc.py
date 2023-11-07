# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import booking_pb2 as booking__pb2


class BookingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBookingByUserID = channel.unary_stream(
                '/Booking/GetBookingByUserID',
                request_serializer=booking__pb2.UserID.SerializeToString,
                response_deserializer=booking__pb2.BookingData.FromString,
                )
        self.AddBookingForUser = channel.unary_unary(
                '/Booking/AddBookingForUser',
                request_serializer=booking__pb2.AddBookingRequest.SerializeToString,
                response_deserializer=booking__pb2.BookingData.FromString,
                )
        self.GetListBookings = channel.unary_stream(
                '/Booking/GetListBookings',
                request_serializer=booking__pb2.EmptyBooking.SerializeToString,
                response_deserializer=booking__pb2.BookingData.FromString,
                )


class BookingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetBookingByUserID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddBookingForUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetListBookings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBookingByUserID': grpc.unary_stream_rpc_method_handler(
                    servicer.GetBookingByUserID,
                    request_deserializer=booking__pb2.UserID.FromString,
                    response_serializer=booking__pb2.BookingData.SerializeToString,
            ),
            'AddBookingForUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AddBookingForUser,
                    request_deserializer=booking__pb2.AddBookingRequest.FromString,
                    response_serializer=booking__pb2.BookingData.SerializeToString,
            ),
            'GetListBookings': grpc.unary_stream_rpc_method_handler(
                    servicer.GetListBookings,
                    request_deserializer=booking__pb2.EmptyBooking.FromString,
                    response_serializer=booking__pb2.BookingData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Booking', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Booking(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetBookingByUserID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Booking/GetBookingByUserID',
            booking__pb2.UserID.SerializeToString,
            booking__pb2.BookingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddBookingForUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/AddBookingForUser',
            booking__pb2.AddBookingRequest.SerializeToString,
            booking__pb2.BookingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetListBookings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Booking/GetListBookings',
            booking__pb2.EmptyBooking.SerializeToString,
            booking__pb2.BookingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
