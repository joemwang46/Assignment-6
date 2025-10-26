from Singleton import Config
from data_loader import YahooFinanceAdapter, BloombergXMLAdapter
from Strategy import MeanReversionStrategy, BreakoutStrategy
from engine import Engine
from reporting import Reporting

def main():
    config = Config("config.json")
    reporting = Reporting()
    adapter_y = YahooFinanceAdapter("external_data_yahoo.json")
    adapter_b = BloombergXMLAdapter("external_data_bloomberg.xml")
    data = [adapter_y.get_data("AAPL"), adapter_b.get_data("MSFT")]
    strategy_name = config.get("default_strategy")
    strategy = MeanReversionStrategy() if strategy_name == "MeanReversionStrategy" else BreakoutStrategy()
    engine = Engine(strategy, reporting.publisher)
    engine.run(data)

if __name__ == "__main__":
    main()
