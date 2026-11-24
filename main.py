import os

# Weirdest job title: a senior corporate role whose entire job is
# apologizing on behalf of self-driving cars.
TITLE = "Senior Apologizer for Self-Driving Cars"

OUTPUT_PATH = "/output/entry.txt"


def write_entry():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TITLE)


write_entry()
