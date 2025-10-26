from models import Observer

class LoggerObserver(Observer):
    def update(self, signal: dict):
        print(f"[LOG] {signal['symbol']} signal: {signal['action']} (strength={signal['strength']})")

class AlertObserver(Observer):
    def update(self, signal: dict):
        if abs(signal.get("strength", 0)) > 1:
            print(f"[ALERT] High-impact signal on {signal['symbol']} → {signal['action'].upper()}")
