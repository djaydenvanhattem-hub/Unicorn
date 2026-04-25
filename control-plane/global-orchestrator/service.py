class GlobalOrchestrator:
    def __init__(self):
        self.services = {}

    def register_service(self, name, metadata):
        self.services[name] = metadata

    def get_services(self):
        return self.services
