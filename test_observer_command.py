import pytest
from Observer import LoggerObserver, AlertObserver
from models import SignalPublisher
from Command import Broker, CommandInvoker, ExecuteOrderCommand

@pytest.fixture
def setup_publisher():
    pub = SignalPublisher()
    log = LoggerObserver()
    alert = AlertObserver()
    pub.attach(log)
    pub.attach(alert)
    return pub

@pytest.fixture
def setup_broker_invoker():
    return Broker(), CommandInvoker()

def test_observer_notifies_and_command_executes(setup_publisher, setup_broker_invoker, capsys):
    broker, invoker = setup_broker_invoker
    cmd = ExecuteOrderCommand(broker, "AAPL", 50, "BUY")
    invoker.execute_command(cmd)
    sig = {"symbol": "AAPL", "action": "BUY", "strength": 2}
    setup_publisher.notify(sig)
    out = capsys.readouterr().out
    assert "AAPL" in out
    assert broker.orders[-1]["action"] == "BUY"
