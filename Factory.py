from datetime import date
from typing import Optional
from models import Instrument

class Stock(Instrument):
    def __init__(self, symbol: str, price: float, sector: str, issuer: str):
        super().__init__(symbol, price, sector, issuer)
        self.type = "Stock"


class Bond(Instrument):
    def __init__(self, symbol: str, price: float, sector: str, issuer: str, 
                 maturity: date):
        super().__init__(symbol, price, sector, issuer, maturity)
        self.type = "Bond"


class ETF(Instrument):
    def __init__(self, symbol: str, price: float, sector: str, issuer: str):
        super().__init__(symbol, price, sector, issuer)
        self.type = "ETF"


class InstrumentFactory:
    @staticmethod
    def create_instrument(security_type: str, symbol: str, price: float, sector: str, issuer: str, maturity: Optional[date] = None):
        if security_type == "Stock":
            return Stock(symbol, price, sector, issuer)
        elif security_type == "Bond":
            return Bond(symbol, price, sector, issuer, maturity)
        elif security_type == "ETF":
            return ETF(symbol, price, sector, issuer)
        else:
            raise ValueError("Unknown security type")