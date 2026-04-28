from doctrine import Doctrine


def build_local_prompt(user_message):
    doctrine = Doctrine.load("standard_public_template")
    receipt = doctrine.mount()
    return receipt["instruction_context"] + "\n\nUser:\n" + user_message + "\n"


def main():
    prompt = build_local_prompt("Give me a concise summary of mounted doctrine.")
    print(prompt)


if __name__ == "__main__":
    main()
