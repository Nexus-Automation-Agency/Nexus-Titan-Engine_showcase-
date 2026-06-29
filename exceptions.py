class NexusTitanError(Exception):
    """Base exception."""


class ValidationError(NexusTitanError):
    """Input validation failed."""


class ConfigurationError(NexusTitanError):
    """Invalid configuration."""
