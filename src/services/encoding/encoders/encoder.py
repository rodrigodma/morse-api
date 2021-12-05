from abc import abstractmethod


class Encoder():
    "encoder abstract class"

    def __init__(self) -> None:
        pass

    @abstractmethod
    def encode(text):
        pass

    @abstractmethod
    def decode(text):
        pass