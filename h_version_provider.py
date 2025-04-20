from pathlib import Path
from commitizen.providers import VersionProvider


class HVersionProvider(VersionProvider):
    file = Path() / "Version.h"

    def get_version(self) -> str:
        return f'{self.file.read_text()}'

    def set_version(self, version: str):
        self.file.write_text(version)