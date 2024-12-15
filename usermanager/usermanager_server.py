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
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import usermanager_pb2
import usermanager_pb2_grpc
userList: list[usermanager_pb2.UserResponse] = []
class UserService(usermanager_pb2_grpc.UserServiceServicer):

    def CreateUser(self, request, context):
        global userList
        try:
            curid = str(int(userList[-1].user_id) + 1)
        except:
            curid = "1"
        curuser = usermanager_pb2.UserResponse(user_id=curid, name=request.name, email=request.email)
        # return usermanager_pb2.UserResponse()
        userList.append(curuser)
        return curuser
    def GetUser(self, request, context):
        global userList
        curuser = usermanager_pb2.UserResponse(user_id='0', name='None', email='None')
        for i in userList:
            if i.user_id == request.user_id:
                curuser = i
        # return usermanager_pb2.UserResponse()
        return curuser


def serve():
    port = "50052"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    usermanager_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
