from pathlib import Path
from commitizen.providers import VersionProvider
import re

class HVersionProvider(VersionProvider):
    file_path = Path() / "Version.h"

    def get_version(self) -> str:
        with open(self.file_path, 'r') as f:
            content = f.read()

            major = re.search(r'#define\s+GAME_VERSION_MAJOR\s+(\d+)', content)
            minor = re.search(r'#define\s+GAME_VERSION_MINOR\s+(\d+)', content)
            patch = re.search(r'#define\s+GAME_VERSION_PATCH\s+(\d+)', content)

            if major and minor and patch:
                return f"{major.group(1)}.{minor.group(1)}.{patch.group(1)}"
            else:
                raise ValueError("Version numbers not found in file.")

    def set_version(self, version: str):
        major, minor, patch = version.split('.')

        content = f"""#pragma once

#define GAME_VERSION_MAJOR {major}
#define GAME_VERSION_MINOR {minor}
#define GAME_VERSION_PATCH {patch}"""

        with open(self.file_path, 'w') as f:
            f.write(content)