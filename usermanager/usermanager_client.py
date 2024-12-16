# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import usermanager_pb2
import usermanager_pb2_grpc

# server_addr = "localhost"
server_addr = "192.168.20.10"

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel(f"{server_addr}:50052") as channel:
        stub = usermanager_pb2_grpc.UserServiceStub(channel)
        response = stub.CreateUser(usermanager_pb2.CreateUserRequest(name="you", email="example@mail.ru"))
    print("CreateUserRequest client received: " + str(response))

    with grpc.insecure_channel(f"{server_addr}:50052") as channel:
        stub = usermanager_pb2_grpc.UserServiceStub(channel)
        response = stub.GetUser(usermanager_pb2.GetUserRequest(user_id='61'))
    print("CreateUserRequest client received: " + str(response))

def create_user(name: str, email: str):
 with grpc.insecure_channel(f"{server_addr}:50052") as channel:
  from usermanager import usermanager_pb2_grpc, usermanager_pb2
  stub = usermanager_pb2_grpc.UserServiceStub(channel)
  response = stub.CreateUser(usermanager_pb2.CreateUserRequest(name=name, email=email))
 out = ("Success: \n" + str(response))
 return out

def get_user(userid: str):
 with grpc.insecure_channel(f"{server_addr}:50052") as channel:
  from usermanager import usermanager_pb2_grpc, usermanager_pb2
  stub = usermanager_pb2_grpc.UserServiceStub(channel)
  response = stub.GetUser(usermanager_pb2.GetUserRequest(userid))
 out = ("Success: \n" + str(response))

 return out

if __name__ == "__main__":
    logging.basicConfig()
    run()
