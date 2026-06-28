from datetime import datetime


class EnterpriseLogger:
    def info(self, message: str) -> None:
        print(f"[INFO] {datetime.now()} | {message}")

    def warning(self, message: str) -> None:
        print(f"[WARNING] {datetime.now()} | {message}")

    def error(self, message: str) -> None:
        print(f"[ERROR] {datetime.now()} | {message}")
