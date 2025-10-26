from models import MarketDataPoint, Strategy

class MeanReversionStrategy(Strategy):
    def __init__(self, lookback_window=20, threshold=0.02):
        self._lookback = lookback_window
        self._threshold = threshold
        self._prices = []

    def generate_signals(self, tick: MarketDataPoint):
        self._prices.append(tick.price)
        if len(self._prices) < self._lookback:
            return 0  # not enough data

        recent = self._prices[-self._lookback:]
        mean = sum(recent) / len(recent)
        deviation = (tick.price - mean) / mean

        if deviation > self._threshold:
            return -1  # price too high → sell
        elif deviation < -self._threshold:
            return 1   # price too low → buy
        else:
            return 0   # no signal

class BreakoutStrategy(Strategy):
    def __init__(self, lookback_window=15, threshold=0.03):
        self._lookback = lookback_window
        self._threshold = threshold
        self._prices = []

    def generate_signals(self, tick: MarketDataPoint):
        self._prices.append(tick.price)
        if len(self._prices) < self._lookback:
            return 0

        recent = self._prices[-self._lookback:]
        high, low = max(recent), min(recent)

        if tick.price > high * (1 + self._threshold):
            return 1  # breakout up
        elif tick.price < low * (1 - self._threshold):
            return -1  # breakout down
        else:
            return 0
