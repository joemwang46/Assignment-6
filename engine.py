from models import SignalPublisher
from Command import Broker, ExecuteOrderCommand, CommandInvoker
from Strategy import MeanReversionStrategy, BreakoutStrategy

class Engine:
    def __init__(self, strategy, publisher):
        self.strategy = strategy
        self.publisher = publisher
        self.broker = Broker()
        self.invoker = CommandInvoker()

    def run(self, data):
        for tick in data:
            signal = self.strategy.generate_signals(tick)
            if signal != 0:
                action = "BUY" if signal == 1 else "SELL"
                s = {"symbol": tick.symbol, "action": action, "strength": signal}
                self.publisher.notify(s)
                cmd = ExecuteOrderCommand(self.broker, tick.symbol, 100, action)
                self.invoker.execute_command(cmd)
