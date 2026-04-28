import json
from doctrine import Doctrine


def build_payload(user_message):
    doctrine = Doctrine.load("standard_public_template")
    receipt = doctrine.mount()
    return {
        "system": receipt["instruction_context"],
        "user": user_message,
        "metadata": {
            "doctrine_id": receipt["id"],
            "context_sha256": receipt["context_sha256"],
        },
    }


def main():
    payload = build_payload("Explain Doctrine Protocol in one paragraph.")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
