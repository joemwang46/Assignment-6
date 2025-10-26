# Design Patterns Used

**Singleton:** Centralized configuration (`Config`) ensures global consistency.

**Factory:** Creates instruments (`InstrumentFactory`) based on type.

**Builder:** Constructs nested portfolios (`PortfolioBuilder`).

**Composite:** Aggregates positions and portfolios recursively.

**Adapter:** Normalizes external data (Yahoo JSON, Bloomberg XML).

**Strategy:** Interchangeable trading logic (MeanReversion, Breakout).

**Observer:** Modular logging and alerts reacting to signals.

**Command:** Encapsulates trade actions with undo/redo potential.

**Decorator:** Extends instrument analytics without altering base class.

Each pattern is modular, easily replaceable, and minimizes coupling.
