# %%
from __future__ import annotations
from polycrystal import PolyFactory

# %%
factory = PolyFactory(200, 300)
factory.seedGrains(18)
factory.growGrains()

# %%
factory.showGrains()


# %%