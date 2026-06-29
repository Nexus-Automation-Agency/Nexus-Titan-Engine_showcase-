from dataclasses import dataclass


@dataclass
class Report:

    status: str
    confidence: float

    def summary(self) -> str:
        return (
            f"Status: {self.status}\n"
            f"Confidence: {self.confidence:.2f}%"
        )
