from setuptools import setup, find_packages

setup(
    name="rev-commit",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
        "rich",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "rev-commit=rev_commit.rev_commit:main",
        ],
    },
)
