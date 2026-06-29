from dataclasses import dataclass


@dataclass(frozen=True)
class EngineConfig:
    VERSION = "1.0.0"
    PLATFORM = "Enterprise"
    MODE = "Public Showcase"
    LICENSE = "Proprietary"
