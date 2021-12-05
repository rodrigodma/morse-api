from services.encoding.encoders.encoder import Encoder
from morse3 import Morse as m

MORSE_ENCODING_NAME = 'morse'

class MorseEncoder(Encoder):
    "morse encoder class"

    def __init__(self) -> None:
        super().__init__()

    def decode(self, text):
        return m(text).morseToString()

    def encode(self, text):
        return m(text).stringToMorse()