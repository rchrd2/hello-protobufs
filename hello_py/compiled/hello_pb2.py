# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hello.proto',
  package='tutorial',
  syntax='proto3',
  serialized_pb=_b('\n\x0bhello.proto\x12\x08tutorial\"\x14\n\x05Hello\x12\x0b\n\x03who\x18\x01 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HELLO = _descriptor.Descriptor(
  name='Hello',
  full_name='tutorial.Hello',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='who', full_name='tutorial.Hello.who', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=45,
)

DESCRIPTOR.message_types_by_name['Hello'] = _HELLO

Hello = _reflection.GeneratedProtocolMessageType('Hello', (_message.Message,), dict(
  DESCRIPTOR = _HELLO,
  __module__ = 'hello_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.Hello)
  ))
_sym_db.RegisterMessage(Hello)


# @@protoc_insertion_point(module_scope)
