# app
from .base import *  # noqa: F401, F403
from .drf import *  # noqa: F401, F403


try:
    from .local import *  # noqa: F401, F403
except ImportError:
    from logging import getLogger
    getLogger(__name__).warning('cannot import local settings, use settings for docker')

    from .local_docker import *  # noqa: F401, F403
