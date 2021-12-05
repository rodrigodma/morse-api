from controller.controller import Controller
from services.encoding.encoders.encoder import Encoder
from services.encoding.encoders.morse.morse_encoder import MORSE_ENCODING_NAME, MorseEncoder
from services.encoding.encoding_service import ENCODING_SERVICE_NAME, EncodingService


class EncodingController(Controller):

    def __init__(self) -> None:
        super().__init__()
        encodingService = EncodingService()
        encodingService.setEncoders(MORSE_ENCODING_NAME, MorseEncoder())
        self.setServices(ENCODING_SERVICE_NAME, encodingService)

    def decode(self, text):
        return self.services[ENCODING_SERVICE_NAME].decode(MORSE_ENCODING_NAME, text)

    def encode(self, text):
        return self.services[ENCODING_SERVICE_NAME].encode(MORSE_ENCODING_NAME, text)