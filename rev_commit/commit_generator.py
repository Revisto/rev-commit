from openai import OpenAI
from rev_commit.config import GITHUB_TOKEN, ENDPOINT, MODEL_NAME

client = OpenAI(
    base_url=ENDPOINT,
    api_key=GITHUB_TOKEN,
)


def generate_commit_message(changes_description):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant for generating commit names."  # noqa
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Generate a commit message using emojis for the following "  # noqa
                        f"changes: {changes_description}"
                    ),
                },
            ],
            temperature=1.0,
            top_p=1.0,
            max_tokens=100,
            model=MODEL_NAME,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise RuntimeError(f"Failed to generate commit message: {str(e)}")
