class Log:
    def __init__(self, level):
        self._level = level

    def __call__(self, message):
        print("{}: {}".format(self._level, message))

log_info = Log("info")
log_warning = Log("warning")
log_error = Log("error")

log_info('Just informational message')