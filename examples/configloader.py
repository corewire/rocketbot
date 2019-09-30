try:
    from bot_config import *  # noqa F401, F403
except ModuleNotFoundError:
    raise Exception(
        'Please provide the login credentials in a bot_config.py (Template available in bot_config.py.dist)') from None
