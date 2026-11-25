import os

def build_line():
    setup = "My worst Monday: deploy frozen, inbox flooded, and a stand-up that should have been a message"
    twist = "my therapist now bills by the sprint."
    return setup + " \u2014 " + twist


LINE = build_line()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
