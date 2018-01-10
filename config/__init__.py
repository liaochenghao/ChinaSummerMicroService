try:
    from config.prod import *
except ImportError:
    from config.dev import *