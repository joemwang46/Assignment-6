import pytest
from Strategy import MeanReversionStrategy, BreakoutStrategy
from models import MarketDataPoint

@pytest.fixture
def ticks():
    return [
        MarketDataPoint(None, "AAPL", 100),
        MarketDataPoint(None, "AAPL", 102),
        MarketDataPoint(None, "AAPL", 98),
        MarketDataPoint(None, "AAPL", 105)
    ]

def test_mean_reversion_behavior(ticks):
    s = MeanReversionStrategy(lookback_window=3, threshold=0.02)
    signals = [s.generate_signals(t) for t in ticks]
    assert all(isinstance(x, int) for x in signals)
    assert any(x != 0 for x in signals)

def test_breakout_behavior(ticks):
    s = BreakoutStrategy(lookback_window=2, threshold=0.01)
    signals = [s.generate_signals(t) for t in ticks]
    assert all(isinstance(x, int) for x in signals)
    assert any(x != 0 for x in signals)
