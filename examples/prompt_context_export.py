from doctrine import Doctrine


def main():
    doctrine = Doctrine.load("standard_public_template")
    receipt = doctrine.mount()

    with open("mounted_context.txt", "w", encoding="utf-8") as output:
        output.write(receipt["instruction_context"])

    print("Wrote mounted_context.txt")


if __name__ == "__main__":
    main()
