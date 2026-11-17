import json
from pathlib import Path

from openai import OpenAI

from .config import apikey, model, model_url


def main():
    project_dir = Path(__file__).resolve().parent

    with (project_dir / "db.json").open(encoding="utf-8") as file:
        data = json.load(file)

    prompt = (project_dir / "prompt.txt").read_text(encoding="utf-8")

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": json.dumps(data, ensure_ascii=False)},
        ],
        "stream": False,
    }

    with OpenAI(
        base_url=model_url,
        api_key=apikey or "local",
        timeout=300.0,
    ) as client:
        response = client.chat.completions.create(**payload)

    print(response.choices[0].message.content)


main()
