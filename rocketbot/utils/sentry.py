import raven

_client = None


def init(sentry_url: str) -> None:
    global _client
    _client = raven.Client(sentry_url)


def exception() -> None:
    if _client:
        _client.captureException()


def message(msg: str) -> None:
    if _client:
        _client.captureMessage(msg)
