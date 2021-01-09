# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculator.proto',
  package='ngrpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x63\x61lculator.proto\x12\x05ngrpc\"(\n\nSumRequest\x12\x0c\n\x04num1\x18\x01 \x01(\x05\x12\x0c\n\x04num2\x18\x02 \x01(\x05\"\x1d\n\x0bSumResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\"\x1c\n\nPNDRequest\x12\x0e\n\x06number\x18\x01 \x01(\x05\"\x1d\n\x0bPNDResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\"\x1d\n\x0e\x41verageRequest\x12\x0b\n\x03num\x18\x01 \x01(\x02\"!\n\x0f\x41verageResponse\x12\x0e\n\x06result\x18\x01 \x01(\x02\"\x1d\n\x0e\x46indMaxRequest\x12\x0b\n\x03num\x18\x01 \x01(\x05\"\x1e\n\x0f\x46indMaxResponse\x12\x0b\n\x03max\x18\x01 \x01(\x05\"\x1c\n\rSquareRequest\x12\x0b\n\x03num\x18\x01 \x01(\x05\"$\n\x0eSquareResponse\x12\x12\n\nsquareRoot\x18\x01 \x01(\x01\x32\xfd\x02\n\x11\x43\x61lculatorService\x12.\n\x03Sum\x12\x11.ngrpc.SumRequest\x1a\x12.ngrpc.SumResponse\"\x00\x12:\n\x0fSumWithDeadline\x12\x11.ngrpc.SumRequest\x1a\x12.ngrpc.SumResponse\"\x00\x12\x45\n\x18PrimeNumberDecomposition\x12\x11.ngrpc.PNDRequest\x1a\x12.ngrpc.PNDResponse\"\x00\x30\x01\x12<\n\x07\x41verage\x12\x15.ngrpc.AverageRequest\x1a\x16.ngrpc.AverageResponse\"\x00(\x01\x12>\n\x07\x46indMax\x12\x15.ngrpc.FindMaxRequest\x1a\x16.ngrpc.FindMaxResponse\"\x00(\x01\x30\x01\x12\x37\n\x06Square\x12\x14.ngrpc.SquareRequest\x1a\x15.ngrpc.SquareResponse\"\x00\x62\x06proto3'
)




_SUMREQUEST = _descriptor.Descriptor(
  name='SumRequest',
  full_name='ngrpc.SumRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num1', full_name='ngrpc.SumRequest.num1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num2', full_name='ngrpc.SumRequest.num2', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=67,
)


_SUMRESPONSE = _descriptor.Descriptor(
  name='SumResponse',
  full_name='ngrpc.SumResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='ngrpc.SumResponse.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=98,
)


_PNDREQUEST = _descriptor.Descriptor(
  name='PNDRequest',
  full_name='ngrpc.PNDRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='ngrpc.PNDRequest.number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=128,
)


_PNDRESPONSE = _descriptor.Descriptor(
  name='PNDResponse',
  full_name='ngrpc.PNDResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='ngrpc.PNDResponse.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=159,
)


_AVERAGEREQUEST = _descriptor.Descriptor(
  name='AverageRequest',
  full_name='ngrpc.AverageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='ngrpc.AverageRequest.num', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=190,
)


_AVERAGERESPONSE = _descriptor.Descriptor(
  name='AverageResponse',
  full_name='ngrpc.AverageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='ngrpc.AverageResponse.result', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=225,
)


_FINDMAXREQUEST = _descriptor.Descriptor(
  name='FindMaxRequest',
  full_name='ngrpc.FindMaxRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='ngrpc.FindMaxRequest.num', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=256,
)


_FINDMAXRESPONSE = _descriptor.Descriptor(
  name='FindMaxResponse',
  full_name='ngrpc.FindMaxResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='max', full_name='ngrpc.FindMaxResponse.max', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=258,
  serialized_end=288,
)


_SQUAREREQUEST = _descriptor.Descriptor(
  name='SquareRequest',
  full_name='ngrpc.SquareRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='ngrpc.SquareRequest.num', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=318,
)


_SQUARERESPONSE = _descriptor.Descriptor(
  name='SquareResponse',
  full_name='ngrpc.SquareResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='squareRoot', full_name='ngrpc.SquareResponse.squareRoot', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=320,
  serialized_end=356,
)

DESCRIPTOR.message_types_by_name['SumRequest'] = _SUMREQUEST
DESCRIPTOR.message_types_by_name['SumResponse'] = _SUMRESPONSE
DESCRIPTOR.message_types_by_name['PNDRequest'] = _PNDREQUEST
DESCRIPTOR.message_types_by_name['PNDResponse'] = _PNDRESPONSE
DESCRIPTOR.message_types_by_name['AverageRequest'] = _AVERAGEREQUEST
DESCRIPTOR.message_types_by_name['AverageResponse'] = _AVERAGERESPONSE
DESCRIPTOR.message_types_by_name['FindMaxRequest'] = _FINDMAXREQUEST
DESCRIPTOR.message_types_by_name['FindMaxResponse'] = _FINDMAXRESPONSE
DESCRIPTOR.message_types_by_name['SquareRequest'] = _SQUAREREQUEST
DESCRIPTOR.message_types_by_name['SquareResponse'] = _SQUARERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SumRequest = _reflection.GeneratedProtocolMessageType('SumRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUMREQUEST,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:ngrpc.SumRequest)
  })
_sym_db.RegisterMessage(SumRequest)

SumResponse = _reflection.GeneratedProtocolMessageType('SumResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUMRESPONSE,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:ngrpc.SumResponse)
  })
_sym_db.RegisterMessage(SumResponse)

PNDRequest = _reflection.GeneratedProtocolMessageType('PNDRequest', (_message.Message,), {
  'DESCRIPTOR' : _PNDREQUEST,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:ngrpc.PNDRequest)
  })
_sym_db.RegisterMessage(PNDRequest)

PNDResponse = _reflection.GeneratedProtocolMessageType('PNDResponse', (_message.Message,), {
  'DESCRIPTOR' : _PNDRESPONSE,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:ngrpc.PNDResponse)
  })
_sym_db.RegisterMessage(PNDResponse)

AverageRequest = _reflection.GeneratedProtocolMessageType('AverageRequest', (_message.Message,), {
  'DESCRIPTOR' : _AVERAGEREQUEST,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:ngrpc.AverageRequest)
  })
_sym_db.RegisterMessage(AverageRequest)

AverageResponse = _reflection.GeneratedProtocolMessageType('AverageResponse', (_message.Message,), {
  'DESCRIPTOR' : _AVERAGERESPONSE,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:ngrpc.AverageResponse)
  })
_sym_db.RegisterMessage(AverageResponse)

FindMaxRequest = _reflection.GeneratedProtocolMessageType('FindMaxRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINDMAXREQUEST,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:ngrpc.FindMaxRequest)
  })
_sym_db.RegisterMessage(FindMaxRequest)

FindMaxResponse = _reflection.GeneratedProtocolMessageType('FindMaxResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINDMAXRESPONSE,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:ngrpc.FindMaxResponse)
  })
_sym_db.RegisterMessage(FindMaxResponse)

SquareRequest = _reflection.GeneratedProtocolMessageType('SquareRequest', (_message.Message,), {
  'DESCRIPTOR' : _SQUAREREQUEST,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:ngrpc.SquareRequest)
  })
_sym_db.RegisterMessage(SquareRequest)

SquareResponse = _reflection.GeneratedProtocolMessageType('SquareResponse', (_message.Message,), {
  'DESCRIPTOR' : _SQUARERESPONSE,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:ngrpc.SquareResponse)
  })
_sym_db.RegisterMessage(SquareResponse)



_CALCULATORSERVICE = _descriptor.ServiceDescriptor(
  name='CalculatorService',
  full_name='ngrpc.CalculatorService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=359,
  serialized_end=740,
  methods=[
  _descriptor.MethodDescriptor(
    name='Sum',
    full_name='ngrpc.CalculatorService.Sum',
    index=0,
    containing_service=None,
    input_type=_SUMREQUEST,
    output_type=_SUMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SumWithDeadline',
    full_name='ngrpc.CalculatorService.SumWithDeadline',
    index=1,
    containing_service=None,
    input_type=_SUMREQUEST,
    output_type=_SUMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PrimeNumberDecomposition',
    full_name='ngrpc.CalculatorService.PrimeNumberDecomposition',
    index=2,
    containing_service=None,
    input_type=_PNDREQUEST,
    output_type=_PNDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Average',
    full_name='ngrpc.CalculatorService.Average',
    index=3,
    containing_service=None,
    input_type=_AVERAGEREQUEST,
    output_type=_AVERAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FindMax',
    full_name='ngrpc.CalculatorService.FindMax',
    index=4,
    containing_service=None,
    input_type=_FINDMAXREQUEST,
    output_type=_FINDMAXRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Square',
    full_name='ngrpc.CalculatorService.Square',
    index=5,
    containing_service=None,
    input_type=_SQUAREREQUEST,
    output_type=_SQUARERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATORSERVICE)

DESCRIPTOR.services_by_name['CalculatorService'] = _CALCULATORSERVICE

# @@protoc_insertion_point(module_scope)