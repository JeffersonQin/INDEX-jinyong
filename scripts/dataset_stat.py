import json
import os


root_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")

files = [
    os.path.join(root_dir, "train.json"),
    os.path.join(root_dir, "test.json"),
    os.path.join(root_dir, "dev.json"),
]

novels = set()
characters = []

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    for k, v in data.items():
        novels.add(v["novel"])
        characters.extend(v["candidate"])

characters = set(characters)

print("list of all novels:", novels)
print("list of characters:", characters)
