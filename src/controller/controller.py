class Controller():

    def __init__(self) -> None:
        self.services = {}

    def setServices(self, serviceName, service):
        self.services[serviceName] = service