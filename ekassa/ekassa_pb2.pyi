from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreatePaymentRequest(_message.Message):
    __slots__ = ("payment_sum", "email")
    PAYMENT_SUM_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    payment_sum: str
    email: str
    def __init__(self, payment_sum: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class PaymentResponse(_message.Message):
    __slots__ = ("payment_id", "payment_sum", "email", "receipt_url")
    PAYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_SUM_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_URL_FIELD_NUMBER: _ClassVar[int]
    payment_id: str
    payment_sum: str
    email: str
    receipt_url: str
    def __init__(self, payment_id: _Optional[str] = ..., payment_sum: _Optional[str] = ..., email: _Optional[str] = ..., receipt_url: _Optional[str] = ...) -> None: ...
