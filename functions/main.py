from firebase_functions import https_fn, logger

message = "🐦‍⬛ Blackbird"


@https_fn.on_request()
def no_logger(req: https_fn.Request) -> https_fn.Response:
    return https_fn.Response("Hello world!" + message)


@https_fn.on_request()
def with_logger(req: https_fn.Request) -> https_fn.Response:
    logger.log(message)
    return https_fn.Response("Hello world!" + message)
