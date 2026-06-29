from typing import Dict, Any


class InputValidator:

    @staticmethod
    def validate(data: Dict[str, Any]) -> bool:
        if not isinstance(data, dict):
            return False

        if not data:
            return False

        return True
