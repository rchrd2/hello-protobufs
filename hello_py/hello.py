#! /usr/bin/python
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "compiled"))

import hello_pb2

hello = hello_pb2.Hello()

print(hello)
print(hello.who)
hello.who = "Richard"
print("Hello, %s!" % hello.who)


from google.protobuf.json_format import MessageToJson
print(MessageToJson(hello))

binary = hello.SerializeToString()
print("binary:")
print(binary)

hello_copy = hello_pb2.Hello()
hello_copy.ParseFromString(binary)
print(MessageToJson(hello_copy))
