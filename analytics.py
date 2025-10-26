from models import Instrument

class InstrumentDecorator:
    def __init__(self, instrument):
        self.instrument = instrument

    def get_metrics(self):
        return self.instrument.get_metrics()

class VolatilityDecorator(InstrumentDecorator):
    def get_metrics(self):
        metrics = super().get_metrics()
        prices = self.instrument.prices
        returns = [(prices[i+1] - prices[i]) / prices[i] for i in range(len(prices)-1)]
        volatility = (sum((r - sum(returns)/len(returns))**2 for r in returns) / len(returns))**0.5
        metrics["volatility"] = round(volatility, 4)
        return metrics


class BetaDecorator(InstrumentDecorator):
    def get_metrics(self):
        metrics = super().get_metrics()
        metrics["beta"] = 1.1
        return metrics


class DrawdownDecorator(InstrumentDecorator):
    def get_metrics(self):
        metrics = super().get_metrics()
        prices = self.instrument.prices
        peak, max_dd = prices[0], 0
        for p in prices:
            peak = max(peak, p)
            dd = (peak - p) / peak
            max_dd = max(max_dd, dd)
        metrics["max_drawdown"] = round(max_dd, 4)
        return metrics
