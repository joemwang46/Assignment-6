from datetime import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass(frozen=True)
class MarketDataPoint:
    timestamp: datetime
    symbol: str
    price: float

class MarketDataAdapter(ABC):
    @abstractmethod
    def get_data(self, symbol: str) -> MarketDataPoint:
        pass

class Instrument:
    def __init__(self, symbol: str, prices: list, sector: str, issuer: str, maturity: Optional[date] = None):
        self.symbol = symbol
        self.prices = prices
        self.sector = sector
        self.issuer = issuer
        self.maturity = maturity

    def get_metrics(self):
        return {"symbol": self.symbol}
    
class Portfolio:
    def __init__(self, name, owner=None, positions=None, subportfolios=None):
        self.name = name
        self.owner = owner
        self.positions = positions or []
        self.subportfolios = subportfolios or []


class PortfolioComponent(ABC):
    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def get_positions(self):
        pass


class Strategy(ABC):
    @abstractmethod
    def generate_signals(self, tick: MarketDataPoint) -> list:
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, signal: dict):
        pass


class SignalPublisher:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, signal: dict):
        for obs in self._observers:
            obs.update(signal)


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass