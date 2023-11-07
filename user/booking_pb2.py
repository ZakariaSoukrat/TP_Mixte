# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: booking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbooking.proto\"\x19\n\x06UserID\x12\x0f\n\x07user_id\x18\x01 \x01(\t\":\n\x0b\x42ookingData\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x1a\n\x05\x64\x61tes\x18\x02 \x03(\x0b\x32\x0b.MovieDates\"*\n\nMovieDates\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t\"D\n\x11\x41\x64\x64\x42ookingRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x10\n\x08movie_id\x18\x03 \x01(\t\"\x0e\n\x0c\x45mptyBooking2\xa7\x01\n\x07\x42ooking\x12/\n\x12GetBookingByUserID\x12\x07.UserID\x1a\x0c.BookingData\"\x00\x30\x01\x12\x37\n\x11\x41\x64\x64\x42ookingForUser\x12\x12.AddBookingRequest\x1a\x0c.BookingData\"\x00\x12\x32\n\x0fGetListBookings\x12\r.EmptyBooking\x1a\x0c.BookingData\"\x00\x30\x01\x62\x06proto3')



_USERID = DESCRIPTOR.message_types_by_name['UserID']
_BOOKINGDATA = DESCRIPTOR.message_types_by_name['BookingData']
_MOVIEDATES = DESCRIPTOR.message_types_by_name['MovieDates']
_ADDBOOKINGREQUEST = DESCRIPTOR.message_types_by_name['AddBookingRequest']
_EMPTYBOOKING = DESCRIPTOR.message_types_by_name['EmptyBooking']
UserID = _reflection.GeneratedProtocolMessageType('UserID', (_message.Message,), {
  'DESCRIPTOR' : _USERID,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:UserID)
  })
_sym_db.RegisterMessage(UserID)

BookingData = _reflection.GeneratedProtocolMessageType('BookingData', (_message.Message,), {
  'DESCRIPTOR' : _BOOKINGDATA,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:BookingData)
  })
_sym_db.RegisterMessage(BookingData)

MovieDates = _reflection.GeneratedProtocolMessageType('MovieDates', (_message.Message,), {
  'DESCRIPTOR' : _MOVIEDATES,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:MovieDates)
  })
_sym_db.RegisterMessage(MovieDates)

AddBookingRequest = _reflection.GeneratedProtocolMessageType('AddBookingRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDBOOKINGREQUEST,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:AddBookingRequest)
  })
_sym_db.RegisterMessage(AddBookingRequest)

EmptyBooking = _reflection.GeneratedProtocolMessageType('EmptyBooking', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYBOOKING,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:EmptyBooking)
  })
_sym_db.RegisterMessage(EmptyBooking)

_BOOKING = DESCRIPTOR.services_by_name['Booking']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USERID._serialized_start=17
  _USERID._serialized_end=42
  _BOOKINGDATA._serialized_start=44
  _BOOKINGDATA._serialized_end=102
  _MOVIEDATES._serialized_start=104
  _MOVIEDATES._serialized_end=146
  _ADDBOOKINGREQUEST._serialized_start=148
  _ADDBOOKINGREQUEST._serialized_end=216
  _EMPTYBOOKING._serialized_start=218
  _EMPTYBOOKING._serialized_end=232
  _BOOKING._serialized_start=235
  _BOOKING._serialized_end=402
# @@protoc_insertion_point(module_scope)
