import pytest
from Factory import InstrumentFactory, Stock, Bond, ETF

def test_factory_creates_instruments():
    stock = InstrumentFactory.create_instrument("Stock", "AAPL", 150, "Tech", "Apple")
    bond = InstrumentFactory.create_instrument("Bond", "US10Y", 100, "Govt", "US Treasury")
    etf = InstrumentFactory.create_instrument("ETF", "SPY", 450, "Index", "State Street")
    assert isinstance(stock, Stock)
    assert isinstance(bond, Bond)
    assert isinstance(etf, ETF)
