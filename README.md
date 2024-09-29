# rev-commit

`rev-commit` is a tool to generate commit messages using OpenAI's GPT-4 model. It helps you create meaningful and emoji-rich commit messages based on the description of changes you provide.

## Installation

To install `rev-commit`, run the following command:

```sh
./install.sh install
```

## Configuration

Before using `rev-commit`, you need to configure your GitHub access token. Open the `rev_commit/config.py` file and replace the placeholder with your actual GitHub access token:

```python
GITHUB_TOKEN = "your_github_access_token_here"
ENDPOINT = "https://models.inference.ai.azure.com"
MODEL_NAME = "gpt-4o"
```

## Usage

To generate a commit message, run the following command:

```sh
rev-commit
```

You will be prompted to enter the description of changes. End the input with two consecutive empty lines to generate the commit message.

## Uninstallation

To uninstall `rev-commit`, run the following command:

```sh
pip uninstall rev-commit
```
or 
```sh
./install.sh uninstall
```