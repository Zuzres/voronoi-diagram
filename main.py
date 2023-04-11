# %%
from __future__ import annotations
from polycrystal import PolyFactory

# %%
factory = PolyFactory(200, 300)
factory.seedCores(18, 3.0)
factory.growGrains()

# %%
factory.showGrains()


# %%