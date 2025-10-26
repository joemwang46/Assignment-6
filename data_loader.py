import csv
from datetime import datetime
import json
import xml.etree.ElementTree as ET
from models import MarketDataPoint, MarketDataAdapter

def load_market_data_from_csv(filename: str):
    datapoints = []

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:          
            datapoint = MarketDataPoint(
                timestamp= datetime.fromisoformat(row['timestamp']),
                symbol=row['symbol'],
                price=float(row['price'])
            )
            datapoints.append(datapoint)

    return datapoints


class YahooFinanceAdapter(MarketDataAdapter):
    def __init__(self, json_path: str):
        with open(json_path, "r") as f:
            self.data = json.load(f)

    def get_data(self, symbol: str) -> MarketDataPoint:
        if self.data["ticker"] != symbol:
            raise ValueError(f"Symbol {symbol} not found in Yahoo data.")
        ts = datetime.fromisoformat(self.data["timestamp"].replace("Z", "+00:00"))
        return MarketDataPoint(timestamp=ts, symbol=self.data["ticker"], price=self.data["last_price"])


class BloombergXMLAdapter(MarketDataAdapter):
    def __init__(self, xml_path: str):
        self.tree = ET.parse(xml_path)
        self.root = self.tree.getroot()

    def get_data(self, symbol: str) -> MarketDataPoint:
        xml_symbol = self.root.find("symbol").text
        if xml_symbol != symbol:
            raise ValueError(f"Symbol {symbol} not found in Bloomberg data.")
        price = float(self.root.find("price").text)
        ts = datetime.fromisoformat(self.root.find("timestamp").text.replace("Z", "+00:00"))
        return MarketDataPoint(timestamp=ts, symbol=xml_symbol, price=price)


def load_strategy_params(path="strategy_params.json"):
    with open(path, "r") as f:
        return json.load(f)