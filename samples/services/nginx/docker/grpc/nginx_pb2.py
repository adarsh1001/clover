# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nginx.proto

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
  name='nginx.proto',
  package='nginx',
  syntax='proto3',
  serialized_pb=_b('\n\x0bnginx.proto\x12\x05nginx\"3\n\x0c\x41lertMessage\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\x12\x11\n\tredis_key\x18\x02 \x01(\t\"w\n\x0b\x43onfigProxy\x12\x13\n\x0bserver_port\x18\x01 \x01(\t\x12\x13\n\x0bserver_name\x18\x02 \x01(\t\x12\x15\n\rlocation_path\x18\x03 \x01(\t\x12\x12\n\nproxy_path\x18\x04 \x01(\t\x12\x13\n\x0bmirror_path\x18\x05 \x01(\t\"\xb7\x01\n\x0c\x43onfigServer\x12\x13\n\x0bserver_port\x18\x01 \x01(\t\x12\x13\n\x0bserver_name\x18\x02 \x01(\t\x12\x11\n\tsite_root\x18\x03 \x01(\t\x12\x12\n\nsite_index\x18\x04 \x01(\t\x12\x1a\n\x12upload_path_config\x18\x05 \x01(\t\x12\x11\n\tlocations\x18\x06 \x01(\t\x12\x18\n\x10upload_path_test\x18\x07 \x01(\t\x12\r\n\x05\x66iles\x18\x08 \x01(\t\"j\n\x08\x43onfigLB\x12\x13\n\x0bserver_port\x18\x01 \x01(\t\x12\x13\n\x0bserver_name\x18\x02 \x01(\t\x12\x10\n\x08slb_list\x18\x03 \x01(\t\x12\x11\n\tslb_group\x18\x04 \x01(\t\x12\x0f\n\x07lb_path\x18\x05 \x01(\t\"\x1d\n\nNginxReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xeb\x01\n\nController\x12\x36\n\x0bModifyProxy\x12\x12.nginx.ConfigProxy\x1a\x11.nginx.NginxReply\"\x00\x12\x38\n\x0cModifyServer\x12\x13.nginx.ConfigServer\x1a\x11.nginx.NginxReply\"\x00\x12\x30\n\x08ModifyLB\x12\x0f.nginx.ConfigLB\x1a\x11.nginx.NginxReply\"\x00\x12\x39\n\rProcessAlerts\x12\x13.nginx.AlertMessage\x1a\x11.nginx.NginxReply\"\x00\x62\x06proto3')
)




_ALERTMESSAGE = _descriptor.Descriptor(
  name='AlertMessage',
  full_name='nginx.AlertMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_id', full_name='nginx.AlertMessage.event_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='redis_key', full_name='nginx.AlertMessage.redis_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=22,
  serialized_end=73,
)


_CONFIGPROXY = _descriptor.Descriptor(
  name='ConfigProxy',
  full_name='nginx.ConfigProxy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_port', full_name='nginx.ConfigProxy.server_port', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_name', full_name='nginx.ConfigProxy.server_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location_path', full_name='nginx.ConfigProxy.location_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proxy_path', full_name='nginx.ConfigProxy.proxy_path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mirror_path', full_name='nginx.ConfigProxy.mirror_path', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=75,
  serialized_end=194,
)


_CONFIGSERVER = _descriptor.Descriptor(
  name='ConfigServer',
  full_name='nginx.ConfigServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_port', full_name='nginx.ConfigServer.server_port', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_name', full_name='nginx.ConfigServer.server_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='site_root', full_name='nginx.ConfigServer.site_root', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='site_index', full_name='nginx.ConfigServer.site_index', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upload_path_config', full_name='nginx.ConfigServer.upload_path_config', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locations', full_name='nginx.ConfigServer.locations', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upload_path_test', full_name='nginx.ConfigServer.upload_path_test', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='files', full_name='nginx.ConfigServer.files', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=197,
  serialized_end=380,
)


_CONFIGLB = _descriptor.Descriptor(
  name='ConfigLB',
  full_name='nginx.ConfigLB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_port', full_name='nginx.ConfigLB.server_port', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_name', full_name='nginx.ConfigLB.server_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slb_list', full_name='nginx.ConfigLB.slb_list', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slb_group', full_name='nginx.ConfigLB.slb_group', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lb_path', full_name='nginx.ConfigLB.lb_path', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=382,
  serialized_end=488,
)


_NGINXREPLY = _descriptor.Descriptor(
  name='NginxReply',
  full_name='nginx.NginxReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='nginx.NginxReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=490,
  serialized_end=519,
)

DESCRIPTOR.message_types_by_name['AlertMessage'] = _ALERTMESSAGE
DESCRIPTOR.message_types_by_name['ConfigProxy'] = _CONFIGPROXY
DESCRIPTOR.message_types_by_name['ConfigServer'] = _CONFIGSERVER
DESCRIPTOR.message_types_by_name['ConfigLB'] = _CONFIGLB
DESCRIPTOR.message_types_by_name['NginxReply'] = _NGINXREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AlertMessage = _reflection.GeneratedProtocolMessageType('AlertMessage', (_message.Message,), dict(
  DESCRIPTOR = _ALERTMESSAGE,
  __module__ = 'nginx_pb2'
  # @@protoc_insertion_point(class_scope:nginx.AlertMessage)
  ))
_sym_db.RegisterMessage(AlertMessage)

ConfigProxy = _reflection.GeneratedProtocolMessageType('ConfigProxy', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGPROXY,
  __module__ = 'nginx_pb2'
  # @@protoc_insertion_point(class_scope:nginx.ConfigProxy)
  ))
_sym_db.RegisterMessage(ConfigProxy)

ConfigServer = _reflection.GeneratedProtocolMessageType('ConfigServer', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGSERVER,
  __module__ = 'nginx_pb2'
  # @@protoc_insertion_point(class_scope:nginx.ConfigServer)
  ))
_sym_db.RegisterMessage(ConfigServer)

ConfigLB = _reflection.GeneratedProtocolMessageType('ConfigLB', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGLB,
  __module__ = 'nginx_pb2'
  # @@protoc_insertion_point(class_scope:nginx.ConfigLB)
  ))
_sym_db.RegisterMessage(ConfigLB)

NginxReply = _reflection.GeneratedProtocolMessageType('NginxReply', (_message.Message,), dict(
  DESCRIPTOR = _NGINXREPLY,
  __module__ = 'nginx_pb2'
  # @@protoc_insertion_point(class_scope:nginx.NginxReply)
  ))
_sym_db.RegisterMessage(NginxReply)



_CONTROLLER = _descriptor.ServiceDescriptor(
  name='Controller',
  full_name='nginx.Controller',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=522,
  serialized_end=757,
  methods=[
  _descriptor.MethodDescriptor(
    name='ModifyProxy',
    full_name='nginx.Controller.ModifyProxy',
    index=0,
    containing_service=None,
    input_type=_CONFIGPROXY,
    output_type=_NGINXREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ModifyServer',
    full_name='nginx.Controller.ModifyServer',
    index=1,
    containing_service=None,
    input_type=_CONFIGSERVER,
    output_type=_NGINXREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ModifyLB',
    full_name='nginx.Controller.ModifyLB',
    index=2,
    containing_service=None,
    input_type=_CONFIGLB,
    output_type=_NGINXREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ProcessAlerts',
    full_name='nginx.Controller.ProcessAlerts',
    index=3,
    containing_service=None,
    input_type=_ALERTMESSAGE,
    output_type=_NGINXREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTROLLER)

DESCRIPTOR.services_by_name['Controller'] = _CONTROLLER

# @@protoc_insertion_point(module_scope)
