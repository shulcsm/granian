class FatalError(Exception):
    ...


class ConfigurationError(FatalError):
    ...


class PidFileError(FatalError):
    ...
