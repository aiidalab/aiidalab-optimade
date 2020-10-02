import warnings

try:
    from aiidalab_widgets_base.databases import OptimadeQueryWidget
except ImportError:
    OptimadeQueryWidget = object

warnings.filterwarnings(action='once')

warnings.warn(
    (
        "Importing OptimadeQueryWidget from `aiidalab_optimade` has been deprecated, "
        "instead import it from `aiidalab_widgets_base`."
    ),
    DeprecationWarning,
)
