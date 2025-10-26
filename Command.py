from models import Command

class Broker:
    def __init__(self):
        self.orders = []

    def execute_order(self, symbol, quantity, action):
        order = {"symbol": symbol, "quantity": quantity, "action": action}
        self.orders.append(order)
        print(f"[EXECUTED] {action} {quantity} shares of {symbol}")

    def cancel_order(self, symbol, quantity, action):
        reverse = {"BUY": "SELL", "SELL": "BUY"}.get(action, "CANCEL")
        print(f"[UNDONE] {reverse} {quantity} shares of {symbol}")
        self.orders.append({"symbol": symbol, "quantity": quantity, "action": reverse})


class ExecuteOrderCommand(Command):
    def __init__(self, broker, symbol, quantity, action):
        self.broker = broker
        self.symbol = symbol
        self.quantity = quantity
        self.action = action

    def execute(self):
        self.broker.execute_order(self.symbol, self.quantity, self.action)

class UndoOrderCommand(Command):
    def __init__(self, broker, symbol, quantity, action):
        self.broker = broker
        self.symbol = symbol
        self.quantity = quantity
        self.action = action

    def execute(self):
        self.broker.cancel_order(self.symbol, self.quantity, self.action)


class CommandInvoker:
    def __init__(self):
        self._history = []
        self._redo_stack = []

    def execute_command(self, command: Command):
        command.execute()
        self._history.append(command)
        self._redo_stack.clear()  # clear redo history on new action

    def undo(self):
        if not self._history:
            print("[INFO] Nothing to undo.")
            return
        command = self._history.pop()
        command.undo()
        self._redo_stack.append(command)

    def redo(self):
        if not self._redo_stack:
            print("[INFO] Nothing to redo.")
            return
        command = self._redo_stack.pop()
        command.execute()
        self._history.append(command)

