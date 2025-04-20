from setuptools import setup

setup(
    name="h_version_provider",
    version="0.1.0",
    py_modules=["h_version_provider"],
    install_requires=["commitizen"],
    entry_points={
        "commitizen.provider": [
            "h-version-provider = h_version_provider:HVersionProvider",
        ]
    },
)