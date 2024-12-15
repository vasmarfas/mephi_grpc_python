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
import random
from concurrent import futures
import logging

import grpc
import ekassa_pb2
import ekassa_pb2_grpc
paymentList: list[ekassa_pb2.PaymentResponse] = []
class PaymentService(ekassa_pb2_grpc.KassaServiceServicer):

    def CreatePayment(self, request, context):
        global paymentList
        try:
            import base64

            sample_string = str(random.randint(9999999999*99999, 9999999999*99999*999999999*999999999))
            sample_string_bytes = sample_string.encode("ascii")

            base64_bytes = base64.b64encode(sample_string_bytes)
            curid = base64_bytes.decode("ascii")

        except:
            curid = "1"
        curpayment = ekassa_pb2.PaymentResponse(payment_id=curid, payment_sum=request.payment_sum, email=request.email, receipt_url=f"https://examplepaymentsystem.com/payment/{curid}")
        # return ekassa_pb2.UserResponse()
        paymentList.append(curpayment)
        return curpayment


def serve():
    port = "50053"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ekassa_pb2_grpc.add_KassaServiceServicer_to_server(PaymentService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
