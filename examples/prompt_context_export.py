from doctrine import Doctrine


def export_context(output_path="mounted_context.txt"):
    doctrine = Doctrine.load("standard_public_template")
    receipt = doctrine.mount()

    with open(output_path, "w", encoding="utf-8") as output:
        output.write(receipt["instruction_context"])

    return output_path


def main():
    output_path = export_context()
    print("Wrote " + str(output_path))


if __name__ == "__main__":
    main()
