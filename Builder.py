from models import Portfolio, PortfolioComponent

class PortfolioBuilder:
    def __init__(self):
        self.name = None
        self.positions = []
        self.owner = None
        self.subportfolios = []

    def add_position(self, symbol, quantity, price):
        self.positions.append({"symbol": symbol, "quantity": quantity, "price": price})
        return self

    def set_owner(self, owner):
        self.owner = owner
        return self

    def add_subportfolio(self, name, builder):
        builder.name = name
        self.subportfolios.append(builder)
        return self

    def build(self):
        built_subs = [sub.build() for sub in self.subportfolios]
        return Portfolio(
            name=self.name,
            owner=self.owner,
            positions=self.positions,
            subportfolios=built_subs
        )

class Position(PortfolioComponent):
    def __init__(self, symbol: str, quantity: float, price: float):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price

    def get_value(self):
        return self.quantity * self.price

    def get_positions(self):
        return [self]

    def __repr__(self):
        return f"Position({self.symbol}, qty={self.quantity}, price={self.price})"


class PortfolioGroup(PortfolioComponent):
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add(self, component: PortfolioComponent):
        self.children.append(component)

    def get_value(self):
        return sum(child.get_value() for child in self.children)

    def get_positions(self):
        positions = []
        for child in self.children:
            positions.extend(child.get_positions())
        return positions

    def __repr__(self):
        return f"PortfolioGroup({self.name}, total_value={self.get_value():.2f})"
