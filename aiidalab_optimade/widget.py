try:
    from aiidalab_widgets_base.databases import OptimadeQueryWidget
except ImportError:
    OptimadeQueryWidget = object

import warnings

warnings.warn(
    (
        "Importing OptimadeQueryWidget from `aiidalab_optimade` has been deprecated, "
        "instead import it from `aiidalab_widgets_base`."
    ),
    DeprecationWarning,
)
