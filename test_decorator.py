import pytest
from analytics import VolatilityDecorator, BetaDecorator, DrawdownDecorator
from models import Instrument

@pytest.fixture
def base_security():
    return Instrument("AAPL", [150, 160, 180], "Tech", "Apple")

def test_decorator_stack(base_security):
    decorated = DrawdownDecorator(BetaDecorator(VolatilityDecorator(base_security)))
    metrics = decorated.get_metrics()
    assert "volatility" in metrics
    assert "beta" in metrics
    assert "drawdown" in metrics
