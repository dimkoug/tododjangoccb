try:
    from .settings_local import *
except ImportError:
    from .settings_base import *
