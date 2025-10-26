from Observer import LoggerObserver, AlertObserver
from models import SignalPublisher

class Reporting:
    def __init__(self):
        self.publisher = SignalPublisher()
        self.logger = LoggerObserver()
        self.alert = AlertObserver()
        self.publisher.attach(self.logger)
        self.publisher.attach(self.alert)
