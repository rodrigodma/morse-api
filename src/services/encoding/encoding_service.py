from services.encoding.encoders.morse.morse_encoder import MORSE_ENCODING_NAME
from services.service import Service

ENCODING_SERVICE_NAME = 'encoding'

class EncodingService(Service):
    "encoding service class"

    def __init__(self) -> None:
        super().__init__()
        self.encoders = {}

    def setEncoders(self, encoderName, encoder):
        self.encoders[encoderName] = encoder

    def decode(self, encoderName, text):
        return self.encoders[encoderName].decode(text)

    def encode(self, encoderName, text):
        return self.encoders[encoderName].encode(text)